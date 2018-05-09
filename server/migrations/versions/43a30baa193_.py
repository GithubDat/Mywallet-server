"""empty message

Revision ID: 43a30baa193
Revises: 
Create Date: 2018-05-08 14:40:50.133406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43a30baa193'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sub_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sub_category_name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sub_category')
    op.drop_table('categorys')
    ### end Alembic commands ###
