"""empty message

Revision ID: 8e7081137dac
Revises: 2b33f414b683
Create Date: 2024-05-12 01:22:16.118198

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e7081137dac'
down_revision: Union[str, None] = '2b33f414b683'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('recipes', 'kitchen',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('recipes', 'kitchen',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###