"""Initial migration

Revision ID: 27a0313caa2e
Revises: dfe5462e5745
Create Date: 2025-01-28 10:20:55.494197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27a0313caa2e'
down_revision: Union[str, None] = 'dfe5462e5745'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mobile', sa.String(length=20), nullable=True),
    sa.Column('number', sa.String(length=6), nullable=True),
    sa.Column('used', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tokens_id'), 'tokens', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tokens_id'), table_name='tokens')
    op.drop_table('tokens')
    # ### end Alembic commands ###
