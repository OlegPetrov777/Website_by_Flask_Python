"""followers

Revision ID: 12eaef751a76
Revises: 3dc984885f78
Create Date: 2020-04-14 11:06:35.103094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12eaef751a76'
down_revision = '3dc984885f78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###