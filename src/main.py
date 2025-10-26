#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
#

"""The entrypoint for the app."""

app: FastAPI = FastAPI(title="My fast API!", description="this is my cool API!")


#   curl http://127.0.0.1:5050/hello-world
@app.get(path="/hello-world")
def hello() -> dict[str, str]:
    return {"Message": "Hello world!"}


#   curl -X POST http://127.0.0.1:5050/hello-world
@app.post(path="/hello-world-post")
def goodbye() -> dict[str, str]:
    return {"Message": "HI have been posted to!"}


#
#  Import LIBRARIES
#  Import FILES
# #
# # if __name__ == "__main__":
# #     uvicorn main:app --port 5050 --reload
