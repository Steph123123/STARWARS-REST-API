"""empty message

Revision ID: 53b3c1280069
Revises: 8950928c20ca
Create Date: 2023-05-09 19:11:12.123873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53b3c1280069'
down_revision = '8950928c20ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fav_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'favorites', ['fav_id'], ['id'])

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('favorites_character_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorites_planets_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorites_vehicles_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.drop_column('planets_id')
        batch_op.drop_column('vehicles_id')
        batch_op.drop_column('character_id')

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fav_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'favorites', ['fav_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('user_fav_id_fkey', type_='foreignkey')
        batch_op.drop_column('fav_id')

    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fav_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'favorites', ['fav_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('fav_id')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fav_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('user_fav_id_fkey', 'favorites', ['fav_id'], ['id'])

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('fav_id')

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('character_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('vehicles_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('planets_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorites_vehicles_id_fkey', 'vehicles', ['vehicles_id'], ['id'])
        batch_op.create_foreign_key('favorites_planets_id_fkey', 'planets', ['planets_id'], ['id'])
        batch_op.create_foreign_key('favorites_character_id_fkey', 'characters', ['character_id'], ['id'])
        batch_op.drop_column('user_id')

    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('fav_id')

    # ### end Alembic commands ###
