"""empty message

Revision ID: d8e818f4ced8
Revises: c28049f3eca6
Create Date: 2022-07-31 16:14:59.590999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8e818f4ced8'
down_revision = 'c28049f3eca6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###
    op.execute('UPDATE todos SET completed = False where completed IS NULL;')
    op.alter_column('todos', 'completed', nullable=False)

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###