"""A module to handle post requests for submitting scores."""

#
#  Import LIBRARIES
from fastapi import APIRouter, HTTPException

#  Import FILES
from ..models.models import Score
from ..processing.addtocsv import add_student_score

#


router: APIRouter = APIRouter()


# #   curl http://127.0.0.1:5050/
@router.get(path="/")
def home() -> dict[str, str]:
    return {"Message": "This is the HOME page"}


# # curl -X 'POST' 'http://127.0.0.1:5050/submit-score' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "John",  "math_score": 66,  "english_score": 85}'
@router.post(path="/submit-score")
def submit_score(score: Score) -> dict[str, str]:
    try:
        add_student_score(name=score.name, math_score=score.math_score, english_score=score.english_score)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Ooops, some error! Error: {exc}")
    return {"Message": f"Details received. Thanks {score.name}"}
