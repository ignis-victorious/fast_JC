#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
# from models.models import Score
from src.routes.submit_scores import router

#

"""The entrypoint for the app."""


def create_app() -> FastAPI:
    """Define a FastAPI Application and add the routes.

    Returns:
        FastAPI: FastAPI: A fastapi object!
    """
    app: FastAPI = FastAPI(title="My fast API!", description="this is my cool API!")
    app.include_router(router=router)
    return app


app: FastAPI = create_app()


# # #   curl http://127.0.0.1:5050/
# @app.get(path="/")
# def home() -> dict[str, str]:
#     return {"Message": "This is the HOME page"}


# # # curl -X 'POST' 'http://127.0.0.1:5050/submit-score' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "John",  "math_score": 66,  "engLish_score": 85}'
# @app.post(path="/submit-score")
# def submit_score(score: Score) -> dict[str, str]:
#     # print("Received {score}!!!")
#     return {"Message": f"Details received. Thanks {score.name}"}
#     # return {"Message": f"I have been posted a score! {score}"}


# #   curl http://127.0.0.1:5050/hello-world
# @app.get(path="/hello-world")
# def hello() -> dict[str, str]:
#     return {"Message": "Hello world!"}


# #   curl -X POST http://127.0.0.1:5050/hello-world-post
# @app.post(path="/hello-world-post")
# def goodbye() -> dict[str, str]:
#     return {"Message": "HI have been posted to!"}


#
#  Import LIBRARIES
#  Import FILES
# #
# # if __name__ == "__main__":
# #     uvicorn main:app --port 5050 --reload
