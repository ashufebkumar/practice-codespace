from fastapi import FastAPI

from app.api.routes import include_routes
from app.core.exceptions import register_exception_handlers
from app.core.lifespan import lifespan
from app.core.logging import setup_logging


def create_app() -> FastAPI:
    app = FastAPI(
        title="Practice Codespace API",
        version="1.0.0",
        description="A scalable FastAPI starter project",
        lifespan=lifespan,
    )

    setup_logging()
    register_exception_handlers(app)
    include_routes(app)

    return app


app = create_app()
