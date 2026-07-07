from pydantic import BaseModel, ConfigDict


# =====================================================
# QUOTATION
# =====================================================

class QuotationCreate(BaseModel):
    quotation_number: str
    customer_id: int
    product_id: int
    quantity: int
    unit_price: float
    total_amount: float


class QuotationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    quotation_number: str
    customer_id: int
    product_id: int
    quantity: int
    unit_price: float
    total_amount: float
    status: str


# =====================================================
# SALES ORDER
# =====================================================

class SalesOrderCreate(BaseModel):
    sales_order_number: str
    quotation_id: int
    customer_id: int
    product_id: int
    quantity: int
    unit_price: float
    total_amount: float


class SalesOrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    sales_order_number: str
    quotation_id: int
    customer_id: int
    product_id: int
    quantity: int
    unit_price: float
    total_amount: float
    status: str


# =====================================================
# INVOICE
# =====================================================

class InvoiceCreate(BaseModel):
    invoice_number: str
    sales_order_id: int
    customer_id: int
    total_amount: float


class InvoiceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    invoice_number: str
    sales_order_id: int
    customer_id: int
    total_amount: float
    payment_status: str
    invoice_status: str