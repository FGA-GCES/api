"""add identifiers

Revision ID: 598cb8aecff8
Revises: 761ca70b556c
Create Date: 2021-06-26 04:10:07.605948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '598cb8aecff8'
down_revision = '761ca70b556c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('accuracy_value', 'value',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
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
    op.add_column('dataset', sa.Column('identifier', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'dataset', ['identifier'])
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
    op.add_column('task', sa.Column('identifier', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'task', ['identifier'])
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
    op.drop_constraint(None, 'task', type_='unique')
    op.drop_column('task', 'identifier')
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
    op.drop_constraint(None, 'dataset', type_='unique')
    op.drop_column('dataset', 'identifier')
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
    op.alter_column('accuracy_value', 'value',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
    # ### end Alembic commands ###
