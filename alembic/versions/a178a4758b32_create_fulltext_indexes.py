"""create fulltext indexes

Revision ID: a178a4758b32
Revises: 75b7754154fe
Create Date: 2026-07-10 23:10:12.519232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a178a4758b32'
down_revision: Union[str, Sequence[str], None] = '75b7754154fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
from alembic import op


def upgrade():

    op.execute("""
        ALTER TABLE products
        ADD FULLTEXT ft_product(name, product_code)
    """)

    op.execute("""
        ALTER TABLE customers
        ADD FULLTEXT ft_customer(company_name, customer_code)
    """)

    op.execute("""
        ALTER TABLE companies
        ADD FULLTEXT ft_company(company_name, company_code)
    """)

    op.execute("""
        ALTER TABLE vendors
        ADD FULLTEXT ft_vendor(name, vendor_code)
    """)

    op.execute("""
        ALTER TABLE employees
        ADD FULLTEXT ft_employee(employee_code, designation)
    """)

    op.execute("""
        ALTER TABLE users
        ADD FULLTEXT ft_user(full_name)
    """)


def downgrade():

    op.execute("ALTER TABLE products DROP INDEX ft_product")
    op.execute("ALTER TABLE customers DROP INDEX ft_customer")
    op.execute("ALTER TABLE companies DROP INDEX ft_company")
    op.execute("ALTER TABLE vendors DROP INDEX ft_vendor")
    op.execute("ALTER TABLE employees DROP INDEX ft_employee")
    op.execute("ALTER TABLE users DROP INDEX ft_user")
