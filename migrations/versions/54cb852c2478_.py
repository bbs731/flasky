"""empty message

Revision ID: 54cb852c2478
Revises: 40a800a2c821
Create Date: 2015-10-17 16:43:46.318407

"""

# revision identifiers, used by Alembic.
revision = '54cb852c2478'
down_revision = '40a800a2c821'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###
