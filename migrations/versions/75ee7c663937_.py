"""empty message

Revision ID: 75ee7c663937
Revises: 
Create Date: 2020-06-18 08:47:37.209546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75ee7c663937'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tool_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tool_type', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('picture', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tools',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tool_name', sa.String(length=50), nullable=False),
    sa.Column('picture', sa.String(length=255), nullable=False),
    sa.Column('website', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('description_link', sa.String(length=255), nullable=False),
    sa.Column('tool_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tool_type_id'], ['tool_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('associated_tools',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('primary_tool_id', sa.Integer(), nullable=False),
    sa.Column('associated_tool_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['associated_tool_id'], ['tools.id'], ),
    sa.ForeignKeyConstraint(['primary_tool_id'], ['tools.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project_tools',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('tool_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['tool_id'], ['tools.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tagged_tools',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('tool_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tool_id'], ['tools.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tagged_tools')
    op.drop_table('project_tools')
    op.drop_table('favorite_projects')
    op.drop_table('associated_tools')
    op.drop_table('tools')
    op.drop_table('projects')
    op.drop_table('users')
    op.drop_table('tool_types')
    # ### end Alembic commands ###
