#
#  Import LIBRARIES
from fastapi import FastAPI, Request, Response

from src.routes.hello_world import router as hello_world

#  Import FILES
# from models.models import Score
from src.routes.receive_file import router as file_router
from src.routes.submit_scores import router as scores_router

#

"""The entrypoint for the app."""


def create_app() -> FastAPI:
    """Define a FastAPI Application and add the routes.

    Returns:
        FastAPI: FastAPI: A fastapi object!
    """
    app: FastAPI = FastAPI(title="My fast API!", description="this is my cool API!")
    app.include_router(router=scores_router)
    app.include_router(router=file_router)
    app.include_router(router=hello_world)

    # Middleware
    @app.middleware(middleware_type="http")
    async def my_middleware(request: Request, call_next):  # -> Any | Response:
        """Some middlware to check the header."""
        if request.headers.get("User") == "Emagnu":
            print(f"Inside middleware - {request.headers.get('User')}")
            # print(f"Inside middleware - {request.headers}")
            response = await call_next(request)
            return response
        return Response(content="Not allowed!\n", status_code=403)

    return app


app: FastAPI = create_app()


#
#  Import LIBRARIES
#  Import FILES
# #
# # if __name__ == "__main__":
# #     uvicorn main:app --port 5050 --reload
