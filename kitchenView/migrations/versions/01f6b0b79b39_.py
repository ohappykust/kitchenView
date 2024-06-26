"""empty message

Revision ID: 01f6b0b79b39
Revises: 
Create Date: 2024-05-11 23:10:20.814591

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01f6b0b79b39'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipes',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('kitchen', sa.String(), nullable=False),
    sa.Column('portions_count', sa.Float(), nullable=False),
    sa.Column('preparation_time_minutes', sa.Integer(), nullable=False),
    sa.Column('cooking_time_minutes', sa.Integer(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('dislikes', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('pin', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('recipe_components',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_nutrition_infos',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('carbohydrates', sa.Float(), nullable=False),
    sa.Column('fats', sa.Float(), nullable=False),
    sa.Column('proteins', sa.Float(), nullable=False),
    sa.Column('kilocalories', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_steps',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_component_measure_units',
    sa.Column('recipe_component_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('name_five', sa.String(), nullable=False),
    sa.Column('name_two', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['recipe_component_id'], ['recipe_components.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_component_measure_units')
    op.drop_table('recipe_steps')
    op.drop_table('recipe_nutrition_infos')
    op.drop_table('recipe_components')
    op.drop_table('users')
    op.drop_table('recipes')
    # ### end Alembic commands ###
