"""Add column cause_id in disruption

Revision ID: 3c0a7038a8c
Revises: 52beb403b32d
Create Date: 2014-07-15 18:25:37.003254

"""

# revision identifiers, used by Alembic.
revision = '3c0a7038a8c'
down_revision = '52beb403b32d'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('disruption', sa.Column('cause_id', postgresql.UUID(), sa.ForeignKey('cause.id')))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('disruption', 'cause_id')
    ### end Alembic commands ###
