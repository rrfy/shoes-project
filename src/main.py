from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI

from config import settings
from presentation.routers.ping import router as ping_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = await asyncpg.connect(settings.postgres.asyncpg_url)
    await conn.close()
    yield


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(ping_router)
    return app
