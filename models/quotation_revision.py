from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base


class QuotationRevision(Base):
    __tablename__ = "quotation_revisions"

    id = Column(Integer, primary_key=True)

    quotation_id = Column(Integer, ForeignKey("quotations.id"))

    revision_number = Column(Integer)

    remarks = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())