from fastapi import APIRouter

from src.api.handlers.links_handler import links_router


def get_apps_router():
    router = APIRouter()
    router.include_router(links_router)
    return router
