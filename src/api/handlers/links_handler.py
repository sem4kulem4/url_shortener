from fastapi import APIRouter

from src.api.schemas import links_schema
from src.api.schemas.base_schema import MessageResponse
from src.services.link_service import link_service

links_router = APIRouter()


@links_router.post("/create_link", response_model=links_schema.LinkCreateResponse)
async def create_link(body: links_schema.LinkCreate):
    """Создает новую короткую ссылку."""
    return await link_service.create(link=body.link)


@links_router.post("/get_link", response_model=links_schema.LinkRetrieveResponse | MessageResponse)
async def get_link(body: links_schema.LinkRetrieve):
    """Возвращает ссылку."""
    return await link_service.get_single(short_link=body.short_link)

@links_router.post("/remove_link", response_model=MessageResponse)
async def remove_link(body: links_schema.LinkDelete):
    """Удаляет ссылку."""
    deleted = await link_service.delete(short_link=body.short_link)
    return {
        "message": (
            f"Ссылка '{body.short_link}' удалена"
            if deleted
            else "Такой ссылки нет!"
        )
    }
