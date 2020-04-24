"""users tables

Revision ID: 6b63cb9f09f6
Revises: 
Create Date: 2020-04-23 00:18:02.387506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b63cb9f09f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service_catalog',
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('service_name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('service_id')
    )
    op.create_index(op.f('ix_service_catalog_service_name'), 'service_catalog', ['service_name'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('roles', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_roles'), 'user', ['roles'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('pricelist',
    sa.Column('price_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['service_catalog.service_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('price_id')
    )
    op.create_table('profile',
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=False),
    sa.Column('about', sa.Text(), nullable=True),
    sa.Column('Instagram', sa.Text(), nullable=False),
    sa.Column('contacts', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('profile_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    op.drop_table('pricelist')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_roles'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_service_catalog_service_name'), table_name='service_catalog')
    op.drop_table('service_catalog')
    # ### end Alembic commands ###
