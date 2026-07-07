from pydantic import BaseModel


class DashboardResponse(BaseModel):

    total_users: int

    total_customers: int

    total_employees: int

    total_products: int

    total_vendors: int

    total_purchase_orders: int

    total_sales_orders: int

    total_invoices: int