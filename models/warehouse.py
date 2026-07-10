from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    warehouse_name = Column(String(150), nullable=False)
    warehouse_code = Column(String(50), unique=True)

    address = Column(String(255))

    is_active = Column(Boolean, default=True)

    zones = relationship(
        "WarehouseZone",
        back_populates="warehouse"
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())