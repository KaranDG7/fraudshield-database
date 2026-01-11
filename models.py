from sqlalchemy import Column, Integer, String, BigInteger
from database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)

    vpa = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)

    mid = Column(BigInteger, nullable=True)     # MID
    mcc = Column(Integer, nullable=True)        # MCC
    geohash = Column(String, nullable=True)

    fraud_reports = Column(Integer, default=0)  # flags
