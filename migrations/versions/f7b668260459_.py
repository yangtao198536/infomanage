"""empty message

Revision ID: f7b668260459
Revises: 57ace35e7e7d
Create Date: 2019-01-22 14:37:55.940143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7b668260459'
down_revision = '57ace35e7e7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(length=64), nullable=True),
    sa.Column('area', sa.String(length=64), nullable=True),
    sa.Column('types', sa.String(length=64), nullable=True),
    sa.Column('version', sa.String(length=64), nullable=True),
    sa.Column('dates', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    # ### end Alembic commands ###
