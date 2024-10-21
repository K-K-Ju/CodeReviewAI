import os

from openai import OpenAI
from fastapi import FastAPI

app = FastAPI()

config = {
    'OPENAI_API_KEY': os.environ.get('OPENAI_API_KEY'),
    'GITHUB_API_KEY': os.environ.get('GITHUB_API_KEY')
}

openai = OpenAI(api_key=config['OPENAI_API_KEY'], project='CodeReviewAI')


@app.get("/")
async def index():
    return {"Hello": "World"}

@app.post("/review")
async def review(assignment_description: str, github_repo_url: str, candidate_level: str):
    messages = {}
    completions = openai.chat.completions.create(
        response_format={},
        model='gpt-4-turbo',
        messages=messages)

    return
