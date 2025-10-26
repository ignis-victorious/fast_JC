#
#  Import LIBRARIES
from fastapi import APIRouter, Response

#  Import FILES
# #


"""The most simplest of endpoints."""

router: APIRouter = APIRouter()


@router.get(path="/hello-world")
async def hello_world(response: Response) -> set[str]:
    """A simple endpoint!"""
    print("Hello World endpoint called", response)
    return {"Hello World"}
