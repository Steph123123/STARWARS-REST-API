"""empty message

Revision ID: 598bebaab14d
Revises: 87e435e0424d
Create Date: 2023-04-21 20:28:40.202923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '598bebaab14d'
down_revision = '87e435e0424d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('rotation_period', sa.String(length=80), nullable=False),
    sa.Column('orbital_period', sa.String(length=80), nullable=False),
    sa.Column('diameter', sa.String(length=80), nullable=False),
    sa.Column('climate', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('model', sa.String(length=80), nullable=False),
    sa.Column('manufacturer', sa.String(length=80), nullable=False),
    sa.Column('cost_in_credits', sa.String(length=80), nullable=False),
    sa.Column('length', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    op.drop_table('planet')
    # ### end Alembic commands ###
