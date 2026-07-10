"""add fulltext indexes

Revision ID: d19bb4faeedd
Revises: c13057430727
Create Date: 2026-07-10 22:57:55.089663

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd19bb4faeedd'
down_revision: Union[str, Sequence[str], None] = 'c13057430727'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
