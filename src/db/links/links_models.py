from sqlalchemy.orm import Mapped, mapped_column

from src.db.base_models import Base


class LinkToShort(Base):
    link: Mapped[str] = mapped_column(unique=True)
    short_link: Mapped[str] = mapped_column(unique=True)
