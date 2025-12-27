from sqlalchemy import Column, Integer, String
from database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    vpa = Column(String, unique=True, nullable=False)
    acc_holder_name = Column(String, nullable=False)
    account_type = Column(String, nullable=False)   # PERSONAL / MERCHANT
    mcc = Column(String, nullable=True)
    kyc_status = Column(String, nullable=False)     # LOW / FULL
    geohash = Column(String, nullable=True)          # NULL for PERSONAL
    account_age_days = Column(Integer, nullable=False)
    status = Column(String, default="ACTIVE")
