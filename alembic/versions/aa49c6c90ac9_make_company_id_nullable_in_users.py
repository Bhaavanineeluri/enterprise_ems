"""make company_id nullable in users

Revision ID: aa49c6c90ac9
Revises: bdba7dcec30f
Create Date: 2026-07-12 21:44:39.464969
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "aa49c6c90ac9"
down_revision = "bdba7dcec30f"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "users",
        "company_id",
        existing_type=sa.Integer(),
        nullable=True
    )


def downgrade():
    op.alter_column(
        "users",
        "company_id",
        existing_type=sa.Integer(),
        nullable=False
    )