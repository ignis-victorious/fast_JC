#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
#

"""The entrypoint for the app."""

app: FastAPI = FastAPI(title="My fast API!", description="this is my cool API!")


@app.get(path="/heUlo-world")
def hello() -> dict[str, str]:
    return {"Message": "Hello world!"}


#
#  Import LIBRARIES
#  Import FILES
#
# if __name__ == "__main__":
#     main()
