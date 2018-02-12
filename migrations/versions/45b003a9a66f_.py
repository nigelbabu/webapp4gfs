"""empty message

Revision ID: 45b003a9a66f
Revises:
Create Date: 2018-02-12 15:32:20.685721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45b003a9a66f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=100), nullable=False),
        sa.Column('token', sa.String(length=1000), nullable=True),
        sa.Column('email', sa.String(length=100), nullable=True),
        sa.Column('name', sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username')
    )
    op.create_table(
        'node_request',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('node_name', sa.String(length=100), nullable=False),
        sa.Column('node_counts', sa.Integer(), nullable=False),
        sa.Column('hours', sa.Integer(), nullable=False),
        sa.Column('pubkey', sa.VARCHAR(length=1024), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'vm',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ip_address', sa.VARCHAR(length=45), nullable=True),
        sa.Column('vm_name', sa.String(length=100), nullable=False),
        sa.Column('details_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('state', sa.String(length=10), nullable=True),
        sa.ForeignKeyConstraint(['details_id'], ['node_request.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vm')
    op.drop_table('node_request')
    op.drop_table('user')
    # ### end Alembic commands ###
