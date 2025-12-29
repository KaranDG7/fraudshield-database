from sqlalchemy import Column, Integer, String
from database import Base  # ← this MUST come from database.py

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)  # ← DO NOT add anything else here

    vpa = Column(String, unique=True, nullable=False)
    acc_holder_name = Column(String, nullable=False)

    account_type = Column(String, nullable=False)
    mcc = Column(String, nullable=True)
    kyc_status = Column(String, nullable=False)
    geohash = Column(String, nullable=True)

    account_age_days = Column(Integer, nullable=False)
    status = Column(String, default="ACTIVE")
    fraud_reports = Column(Integer, default=0)
