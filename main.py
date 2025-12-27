from fastapi import FastAPI, HTTPException
from database import SessionLocal, engine
from models import Base, Account
import os

# Create tables on startup (Render-safe)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FraudShield Reference Backend")

@app.get("/")
def root():
    return {"status": "FraudShield backend running"}

@app.get("/api/account/{vpa}")
def get_account(vpa: str):
    db = SessionLocal()
    account = db.query(Account).filter(Account.vpa == vpa).first()
    db.close()

    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    return {
        "vpa": account.vpa,
        "acc_holder_name": account.acc_holder_name,
        "account_type": account.account_type,
        "mcc": account.mcc,
        "kyc_status": account.kyc_status,
        "geohash": account.geohash,
        "account_age_days": account.account_age_days,
        "status": account.status
    }
