"""empty message

Revision ID: 705b439f61a4
Revises: 8a957b08274d
Create Date: 2019-05-25 15:15:18.018991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '705b439f61a4'
down_revision = '8a957b08274d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('slug', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'slug')
    # ### end Alembic commands ###
