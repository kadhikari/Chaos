""" Create table wording

Revision ID: 4f7b1b385510
Revises: 4ddbd7d83e6a
Create Date: 2015-01-19 15:16:51.245609

"""

# revision identifiers, used by Alembic.
revision = '4f7b1b385510'
down_revision = '4ddbd7d83e6a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wording',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('key', sa.Text(), nullable=False),
    sa.Column('value', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('associate_wording_cause',
    sa.Column('wording_id', postgresql.UUID(), nullable=False),
    sa.Column('cause_id', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['cause_id'], ['cause.id'], ),
    sa.ForeignKeyConstraint(['wording_id'], ['wording.id'], ),
    sa.PrimaryKeyConstraint('wording_id', 'cause_id', name='wording_cause_pk')
    )

    connection = op.get_bind()
    connection.execute('insert into  wording (created_at, id, key, value) '
                       'select created_at , id ,  \'external_long\', wording from cause')

    connection.execute('insert into  associate_wording_cause (wording_id, cause_id) '
                       'SELECT id, id from cause')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('associate_wording_cause')
    op.drop_table('wording')
    ### end Alembic commands ###