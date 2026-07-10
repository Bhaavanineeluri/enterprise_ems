"""add fulltext indexes

Revision ID: c13057430727
Revises: 8c78ba5e075b
Create Date: 2026-07-10 22:57:01.381220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c13057430727'
down_revision: Union[str, Sequence[str], None] = '8c78ba5e075b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
