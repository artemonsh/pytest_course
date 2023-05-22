"""Initial revision

Revision ID: 9b6ff45d5de5
Revises: 
Create Date: 2023-05-23 00:09:16.476677

"""
from alembic import op
import sqlalchemy as sa


revision = '9b6ff45d5de5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('candies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=200), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.Column('state', sa.String(length=20), server_default='full', nullable=True),
        sa.Column('kid', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('candies')
