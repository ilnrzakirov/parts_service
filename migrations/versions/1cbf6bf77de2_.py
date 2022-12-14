"""

Revision ID: 1cbf6bf77de2
Revises: 04ad1ab180df
Create Date: 2022-10-18 21:21:11.740617

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '1cbf6bf77de2'
down_revision = '04ad1ab180df'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('balance', sa.Integer(), nullable=False),
        sa.Column('company', sa.Integer(), nullable=True),
        sa.Column('name', sa.VARCHAR(length=255), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['company'], ['companies.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
