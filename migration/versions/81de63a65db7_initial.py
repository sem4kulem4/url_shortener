"""initial

Revision ID: 81de63a65db7
Revises: 
Create Date: 2024-10-21 22:23:16.792864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81de63a65db7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('linktoshorts',
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('short_link', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link'),
    sa.UniqueConstraint('short_link')
    )
    op.create_index(op.f('ix_linktoshorts_id'), 'linktoshorts', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_linktoshorts_id'), table_name='linktoshorts')
    op.drop_table('linktoshorts')
    # ### end Alembic commands ###
