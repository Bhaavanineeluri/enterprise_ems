from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class WarehouseZone(Base):
    __tablename__ = "warehouse_zones"

    id = Column(Integer, primary_key=True)

    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))

    zone_name = Column(String(100))
    zone_code = Column(String(50))

    warehouse = relationship(
        "Warehouse",
        back_populates="zones"
    )

    bins = relationship(
        "WarehouseBin",
        back_populates="zone"
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())