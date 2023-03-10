"""3

Revision ID: d74e5ba6ec60
Revises: ac3cd4f84d29
Create Date: 2023-01-11 19:31:32.714408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd74e5ba6ec60'
down_revision = 'ac3cd4f84d29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('last_name', sa.String(length=128), nullable=False),
    sa.Column('phone_number', sa.String(length=128), nullable=False),
    sa.Column('address', sa.String(length=128), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('address')
    # ### end Alembic commands ###
