from pydantic import BaseModel


class LinkShort(BaseModel):
    short_link: str


class LinkCreate(BaseModel):
    link: str


class LinkCreateResponse(LinkShort):
    pass


class LinkRetrieve(LinkShort):
    pass


class LinkRetrieveResponse(LinkShort):
    link: str


class LinkDelete(LinkShort):
    pass
