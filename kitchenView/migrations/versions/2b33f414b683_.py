"""empty message

Revision ID: 2b33f414b683
Revises: 92a3e0aab181
Create Date: 2024-05-12 00:33:55.468676

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b33f414b683'
down_revision: Union[str, None] = '92a3e0aab181'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_name_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_name_key', 'users', ['name'])
    # ### end Alembic commands ###
