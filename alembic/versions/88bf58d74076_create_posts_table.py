"""create posts table

Revision ID: 88bf58d74076
Revises: 
Create Date: 2021-11-25 16:35:42.398411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88bf58d74076'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
