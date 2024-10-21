class BaseService:
    def __init__(self, dal) -> None:
        self.dal = dal

    async def create(self, model):
        return await self.dal.create(data=model.model_dump())

    async def delete(self, **filters) -> None:
        return await self.dal.delete(**filters)

    async def get_single(self, **filters):
        return await self.dal.get_single(**filters)
