"""empty message

Revision ID: 154a23dbff56
Revises: fa9acf32931d
Create Date: 2021-06-17 05:50:03.658467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '154a23dbff56'
down_revision = 'fa9acf32931d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accuracy_value', sa.Column('value', sa.Float(precision=3), nullable=True))
    op.drop_column('accuracy_value', 'values')
    op.alter_column('cpu', 'frequency',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
    op.alter_column('cpu', 'tdp',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
    op.alter_column('cpu', 'gflops',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
    op.alter_column('gpu', 'tdp',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
    op.alter_column('gpu', 'gflops',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
    op.alter_column('model', 'hardware_burden',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
    op.alter_column('model', 'gflops',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
    op.alter_column('model', 'multiply_adds',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
    op.alter_column('tpu', 'tdp',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
    op.alter_column('tpu', 'gflops',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tpu', 'gflops',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('tpu', 'tdp',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('model', 'multiply_adds',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('model', 'gflops',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('model', 'hardware_burden',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('gpu', 'gflops',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('gpu', 'tdp',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('cpu', 'gflops',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('cpu', 'tdp',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('cpu', 'frequency',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    op.add_column('accuracy_value', sa.Column('values', sa.REAL(), autoincrement=False, nullable=True))
    op.drop_column('accuracy_value', 'value')
    # ### end Alembic commands ###
