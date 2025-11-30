import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(task):
    prompt = f"Create a list of sub-tasks from the following task: {task}, one for line with a '-' prefix."
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates simple task lists."},
            {"role": "user", "content": f"Create a simple task list based on the following prompt: {prompt}"}
        ],
        max_tokens=300,
        verbosity="medium",
        reasoning_effort="minimal"
    )
    tasks_text = response.choices[0].message.content
    tasks = [line.strip("- ").strip() for line in tasks_text.split("\n") if line.strip()]
    return tasks