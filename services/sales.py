from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.quotation import Quotation
from models.sales_order import SalesOrder
from models.invoice import Invoice
from models.customer import Customer
from models.product import Product
from models.inventory import Inventory


# =====================================================
# CREATE QUOTATION
# =====================================================

def create_quotation(db: Session, data):

    customer = db.query(Customer).filter(
        Customer.id == data.customer_id
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    product = db.query(Product).filter(
        Product.id == data.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    quotation = Quotation(
        quotation_number=data.quotation_number,
        customer_id=data.customer_id,
        product_id=data.product_id,
        quantity=data.quantity,
        unit_price=data.unit_price,
        total_amount=data.total_amount,
        status="Pending"
    )

    db.add(quotation)
    db.commit()
    db.refresh(quotation)

    return quotation


# =====================================================
# GET QUOTATIONS
# =====================================================

def get_quotations(db: Session):
    return db.query(Quotation).all()


# =====================================================
# CREATE SALES ORDER
# =====================================================

def create_sales_order(db: Session, data):

    quotation = db.query(Quotation).filter(
        Quotation.id == data.quotation_id
    ).first()

    if not quotation:
        raise HTTPException(
            status_code=404,
            detail="Quotation not found"
        )

    inventory = db.query(Inventory).filter(
        Inventory.product_id == data.product_id
    ).first()

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    if inventory.quantity < data.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient inventory"
        )

    inventory.quantity -= data.quantity

    quotation.status = "Approved"

    order = SalesOrder(
        sales_order_number=data.sales_order_number,
        quotation_id=data.quotation_id,
        customer_id=data.customer_id,
        product_id=data.product_id,
        quantity=data.quantity,
        unit_price=data.unit_price,
        total_amount=data.total_amount,
        status="Completed"
    )

    db.add(order)

    db.commit()
    db.refresh(order)

    return order


# =====================================================
# GET SALES ORDERS
# =====================================================

def get_sales_orders(db: Session):
    return db.query(SalesOrder).all()


# =====================================================
# CREATE INVOICE
# =====================================================

def create_invoice(db: Session, data):

    order = db.query(SalesOrder).filter(
        SalesOrder.id == data.sales_order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Sales Order not found"
        )

    invoice = Invoice(
        invoice_number=data.invoice_number,
        sales_order_id=data.sales_order_id,
        customer_id=data.customer_id,
        total_amount=data.total_amount,
        payment_status="Pending",
        invoice_status="Generated"
    )

    db.add(invoice)

    db.commit()
    db.refresh(invoice)

    return invoice


# =====================================================
# GET INVOICES
# =====================================================

def get_invoices(db: Session):
    return db.query(Invoice).all()