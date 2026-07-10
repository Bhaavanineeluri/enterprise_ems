from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class WarehouseBin(Base):
    __tablename__ = "warehouse_bins"

    id = Column(Integer, primary_key=True)

    zone_id = Column(Integer, ForeignKey("warehouse_zones.id"))

    bin_code = Column(String(50))
    shelf = Column(String(50))
    rack = Column(String(50))

    zone = relationship(
        "WarehouseZone",
        back_populates="bins"
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())