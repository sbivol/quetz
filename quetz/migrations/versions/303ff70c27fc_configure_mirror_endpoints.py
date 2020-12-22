"""configure mirror endpoints

Revision ID: 303ff70c27fc
Revises: 8dfb7c4bfbd7
Create Date: 2020-12-22 17:35:45.164946

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '303ff70c27fc'
down_revision = '8dfb7c4bfbd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'channel_mirrors', sa.Column('api_endpoint', sa.String(), nullable=False)
    )
    op.add_column(
        'channel_mirrors', sa.Column('metrics_endpoint', sa.String(), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('channel_mirrors', 'metrics_endpoint')
    op.drop_column('channel_mirrors', 'api_endpoint')
    # ### end Alembic commands ###