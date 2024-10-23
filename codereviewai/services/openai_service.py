from fastapi import HTTPException

import openai
from count_tokens import count_tokens_in_string

from codereviewai import static
from codereviewai.config import settings

openai.api_key = settings.openai_api_key

async def analyze_repo(repo_content, assignment_description, candidate_level):
    prompt = static.REQUEST_TEXT_TEMPLATE.format(candidate_level=candidate_level)
    if count_tokens_in_string(prompt) + count_tokens_in_string(repo_content) + count_tokens_in_string(assignment_description) > 120_000:
        raise HTTPException(status_code=400, detail='Repository contains too many items or assignment description is too long')

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
