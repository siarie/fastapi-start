from fastapi import FastAPI

from .routes import default, users


def create_app():
    app = FastAPI()

    # include api router
    app.include_router(default.router)
    app.include_router(users.router)

    return app


app = create_app()
