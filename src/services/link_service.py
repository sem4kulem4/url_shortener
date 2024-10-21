import random
from string import ascii_lowercase

from fastapi import HTTPException

from src.config.base_config import SHORT_DOMAIN
from src.db.links.links_dal import link_dal
from src.services.base_service import BaseService


class LinkService(BaseService):
    def __init__(self):
        super().__init__(dal=link_dal)

    async def get_single(self, **filters):
        link = await self.dal.get_single(**filters)
        if not link:
            raise HTTPException(status_code=400, detail="Короткой ссылки не существует!")
        return link

    async def create(self, link: str):
        current_link = await self.dal.get_single(link=link)
        if current_link:
            raise HTTPException(status_code=400, detail="Короткая ссылка для текущего ввода уже существует!")
        short = await self.generate_short_link()
        return await self.dal.create(link=link, short_link=short)

    async def generate_short_link(self):
        symbols = [str(i) for i in range(9)] + list(ascii_lowercase)
        while True:
            short = SHORT_DOMAIN + "".join(random.choices(symbols, k=4))
            shortener = await self.dal.get_single(short_link=short)
            if not shortener:
                break
        return short


link_service = LinkService()
