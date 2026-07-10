"""add fulltext indexes

Revision ID: 75b7754154fe
Revises: d19bb4faeedd
Create Date: 2026-07-10 22:58:12.797528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75b7754154fe'
down_revision: Union[str, Sequence[str], None] = 'd19bb4faeedd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
