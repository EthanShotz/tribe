"""Add thread table

Revision ID: 3a8a5f819c5f
Revises: 3b4636df4c6d
Create Date: 2024-05-25 13:57:57.773217

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '3a8a5f819c5f'
down_revision = '3b4636df4c6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('thread',
    sa.Column('query', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_thread_id'), 'thread', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_thread_id'), table_name='thread')
    op.drop_table('thread')
    # ### end Alembic commands ###