"""answers table

Revision ID: b6e39774412e
Revises: 04c59df74853
Create Date: 2020-05-09 15:54:51.721240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6e39774412e'
down_revision = '04c59df74853'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'answer', type_='foreignkey')
    op.create_foreign_key(None, 'answer', 'post', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'answer', type_='foreignkey')
    op.create_foreign_key(None, 'answer', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
