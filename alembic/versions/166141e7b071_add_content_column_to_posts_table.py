"""add content column to posts table

Revision ID: 166141e7b071
Revises: 88bf58d74076
Create Date: 2021-11-25 16:38:19.927880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '166141e7b071'
down_revision = '88bf58d74076'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
