"""Initial migration

Revision ID: 14f7be73acfc
Revises: e7268a1b23bb
Create Date: 2024-06-18 08:35:48.903283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14f7be73acfc'
down_revision = 'e7268a1b23bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('openroles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('job_type', sa.String(), nullable=False),
    sa.Column('duration', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('postroles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('job_type', sa.String(), nullable=False),
    sa.Column('duration', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('role_name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.Column('postrole_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['postrole_id'], ['postroles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('postroles')
    op.drop_table('openroles')
    # ### end Alembic commands ###