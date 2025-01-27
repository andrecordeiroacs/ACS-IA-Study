from openai import OpenAI
from browser_use import Agent, Browser, BrowserConfig, Controller
from langchain_openai import ChatOpenAI
import asyncio
import os
from dotenv import load_dotenv

# Testando aqui a eficiência do Deepseek-reasoner vs GPT4o com browser-use

# Load environment variables
load_dotenv()

# Initialize DeepSeek client
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


async def validate_result(user_query: str, result: str) -> str:
    """Validate the result using DeepSeek's analysis"""
    validation_prompt = f"""
    Original query: {user_query}
    Browser-obtained result: {result}
    
    As a quality validator, check if:
    1. The result directly answers the query
    2. Contains reasonable values/format
    3. Doesn't include browser automation artifacts
    
    Respond in this format:
    Validation: [OK/ERROR]
    Notes: [Brief explanation]
    """
    
    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[{
            "role": "system",
            "content": "You are a quality assurance specialist analyzing browser automation results."
        }, {
            "role": "user",
            "content": validation_prompt
        }],
        temperature=0.2
    )
    
    return response.choices[0].message.content

async def run_task(user_query: str):
    browser = None
    try:
        # Step 1: Generate browser automation plan
        messages = [{
            "role": "system",
            "content": """Convert requests into browser steps. Format:
            1. Action [selector] "input/text"
            Include navigation, clicks, typing, and data saving."""
        }, {
            "role": "user",
            "content": f"Task: {user_query}\nProvide only numbered steps."
        }]

        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=messages,
            temperature=0.3
        )

        plan = response.choices[0].message.content
        print("Generated Plan:\n", plan)

        # Step 2: Configure browser
        browser = Browser(
            config=BrowserConfig(
                headless=False,
                disable_security=True
            )
        )

        # Step 3: Execute plan
        controller = Controller()
        # GPT
        # agent = Agent(
        #     task=plan,
        #     llm=ChatOpenAI(model="gpt-4o"),
        #     controller=controller,
        #     browser=browser
        # )
        
        #DS
        agent = Agent(
            task=plan,
            llm=ChatOpenAI(
			    base_url='https://api.deepseek.com/v1',
			    model='deepseek-reasoner',
			    api_key=os.getenv("DEEPSEEK_API_KEY"),
		    ),
		    use_vision=False,
		    max_failures=2,
		    max_actions_per_step=1,
        )
        result = await agent.run()
        
        # Step 4: Validate result
        validation = await validate_result(user_query, result)
        print("\nValidation Result:\n", validation)
        
        # Step 5: Format final response
        return (
            f"✅ Task Completed!\n"
            f"Result:\n{result}\n\n"
            f"🔍 Quality Check:\n{validation}"
        )

    except Exception as e:
        return f"❌ Error: {str(e)}"
    
    finally:
        if browser:
            await browser.close()

# Example usage
if __name__ == "__main__":
    task = "Encontre 3 preços para a camera de vídeo Insta360 X4."
    result = asyncio.run(run_task(task))
    print(result)
