from fastapi import FastAPI
from starlette import responses

from .config.db import Model, engine


def create_app():
    """
        Creating and configuring our app
    """

    #Creating Database
    Model.metadata.create_all(bind=engine)

    #Creating the API app
    app = FastAPI()

    from .entradas.routes import route as entrada_route

    app.include_router(
        entrada_route,
        prefix='/entrada',
        responses={404: {"description": "not found"}}
    )


    return app