import openai
from codereviewai import static
from config import settings
import json

openai.api_key = settings.openai_api_key

async def analyze_repo(repo_content, assignment_description, candidate_level):
    prompt = static.REQUEST_TEXT_TEMPLATE.format(candidate_level=candidate_level)

    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content":[{"type": "text", "text": "You are a code review assistant."}]},
            {"role": "user", "content": [{"type": "text", "text": prompt}]},
            {"role": "user", "content": [{"type": "text", "text": f"Assignment:{assignment_description}"}]},
            {"role": "user", "content": [{"type": "text", "text": f"Repo content:{repo_content}"}]},
        ],
    )

    review_result = response.choices[0].message['content']
    return review_result
