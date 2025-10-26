#
#  Import LIBRARIES
from fastapi import APIRouter

# from fastapi import APIRouter, Response

#  Import FILES
# #


"""The most simplest of endpoints."""

router: APIRouter = APIRouter()


@router.get(path="/hello-world/{value}/{more}")
async def hello_world(
    value: str, more: str, name: str = "Leonardo", city: str = "Da Vinci", employed: bool = False
) -> set[str]:
    """A simple endpoint!"""
    print("TEST", value, more)
    print(f"Name: {name.title()}, City: {city.title()}")
    return {f"Hello World.. {name.title()},  {city.title()}, {employed}"}


# @router.get(path="/hello-world")
# async def hello_world(name: str = "Leonardo", city: str = "Da Vinci", employed: bool = False) -> set[str]:
#     """A simple endpoint!"""
#     print(f"Name: {name.title()}, City: {city.title()}")
#     return {f"Hello World.. {name.title()},  {city.title()}, {employed}"}


# @router.get(path="/hello-world")
# async def hello_world(name: str, city: str) -> set[str]:
#     """A simple endpoint!"""
#     print(f"Name: {name.title()}, City: {city.title()}")
#     return {f"Hello World.. {name.title()},  {city.title()}"}


# @router.get(path="/hello-world")
# async def hello_world(name: str) -> set[str]:
#     """A simple endpoint!"""
#     print(f"Name: {name.title()}")
#     return {f"Hello World.. {name.title()}"}


# @router.get(path="/hello-world")
# async def hello_world(response: Response) -> set[str]:
#     """A simple endpoint!"""
#     print("Hello World endpoint called", response)
#     return {"Hello World"}
