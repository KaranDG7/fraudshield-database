from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Account

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FraudShield Reference Backend")

@app.get("/")
def root():
    return {"status": "FraudShield backend running"}

@app.get("/api/account/{vpa}")
def get_account(vpa: str):
    db: Session = SessionLocal()

    account = db.query(Account).filter(Account.vpa == vpa).first()
    db.close()

    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    return {
        "vpa": account.vpa,
        "name": account.name,
        "mid": account.mid,
        "mcc": account.mcc,
        "geohash": account.geohash,
        "flags": account.fraud_reports
    }
