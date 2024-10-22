import pydantic_core
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl, Field
from codereviewai.services.github_service import get_repo_contents
from codereviewai.services.openai_service import analyze_repo

router = APIRouter()


class ReviewRequest(BaseModel):
    assignment_description: str
    github_repo_url: HttpUrl
    candidate_level: str = Field(pattern="^Junior|Middle|Senior$")


@router.post("/review")
async def review_code(request: ReviewRequest):
    owner, repo = __parse_repo_url__(request.github_repo_url)
    try:
        repo_content = await get_repo_contents(owner, repo)

        analysis_str = await analyze_repo(
            repo_content=repo_content,
            assignment_description=request.assignment_description,
            candidate_level=request.candidate_level
        )

        return {'analysis': analysis_str}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def __parse_repo_url__(repo_url: pydantic_core.Url):
    l = repo_url.path.split("/")
    if len(l) != 3:
        raise HTTPException(status_code=400, detail="Invalid repo url")
    return l[1], l[2]