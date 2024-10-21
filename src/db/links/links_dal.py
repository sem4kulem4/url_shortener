from src.config.db_helper import db_helper
from src.db.base_dal import BaseDAL
from src.db.links.links_models import LinkToShort


class ShortenerDAL(BaseDAL):
    def __init__(self, db_session):
        super().__init__(model=LinkToShort, db_session=db_session)


link_dal = ShortenerDAL(db_session=db_helper.get_db_session)
