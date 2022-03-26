"""empty message

Revision ID: 1a8506fe9431
Revises: 982b1fc70104
Create Date: 2022-03-25 22:16:57.725388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a8506fe9431'
down_revision = '982b1fc70104'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('funcionario_projeto',
    sa.Column('projeto_id', sa.Integer(), nullable=False),
    sa.Column('funcionario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['funcionario_id'], ['funcionario.id'], ),
    sa.ForeignKeyConstraint(['projeto_id'], ['projeto.id'], ),
    sa.PrimaryKeyConstraint('projeto_id', 'funcionario_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('funcionario_projeto')
    # ### end Alembic commands ###
