"""

Revision ID: 5b3574e0454e
Revises: aeb3ba50f07e
Create Date: 2022-10-26 18:29:52.235055

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '5b3574e0454e'
down_revision = 'aeb3ba50f07e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_superuser', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('is_stuf', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_stuf')
    op.drop_column('users', 'is_superuser')
    # ### end Alembic commands ###
