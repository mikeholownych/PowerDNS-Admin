"""Initial migration to SQLAlchemy 2.0 style models."""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0001_sqlalchemy2_modernization"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column("user", sa.Column("created_at", sa.DateTime(), nullable=True))
    op.add_column("user", sa.Column("updated_at", sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column("user", "updated_at")
    op.drop_column("user", "created_at")
