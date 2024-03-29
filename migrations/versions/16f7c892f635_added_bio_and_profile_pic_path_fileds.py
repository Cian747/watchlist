"""Added bio and profile pic path fileds

Revision ID: 16f7c892f635
Revises: 85b2ef5965e3
Create Date: 2021-08-11 11:17:48.309885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16f7c892f635'
down_revision = '85b2ef5965e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
