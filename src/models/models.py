#
#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
# #


class Score(BaseModel):
    """A model to represent a score."""

    name: str
    math_score: int
    english_score: int
