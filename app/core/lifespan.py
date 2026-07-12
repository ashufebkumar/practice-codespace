import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

logger = logging.getLogger("app")


class AppResource:
    def __init__(self) -> None:
        self.initialized = False

    def initialize(self) -> None:
        self.initialized = True

    def shutdown(self) -> None:
        self.initialized = False


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    logger.info("Application startup")
    app.state.started = True
    app.state.resource = AppResource()
    app.state.resource.initialize()

    try:
        yield
    finally:
        app.state.resource.shutdown()
        app.state.started = False
        logger.info("Application shutdown")
