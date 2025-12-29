import csv
from database import Base, engine, SessionLocal
from models import Account

Base.metadata.create_all(bind=engine)

def seed_accounts():
    db = SessionLocal()

    with open("fraudshield_accounts.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            account = Account(
                vpa=row["vpa"],
                acc_holder_name=row["acc_holder_name"],
                account_type=row["account_type"],
                mcc=row.get("mcc") or None,
                kyc_status=row["kyc_status"],
                geohash=row.get("geohash") or None,
                account_age_days=int(row["account_age_days"]) if row["account_age_days"] else 0,
                status=row.get("status", "ACTIVE"),
                fraud_reports=int(row["fraud_reports"]) if row.get("fraud_reports") else 0
            )
            db.add(account)

    db.commit()
    db.close()
    print("✅ Database seeded successfully")

if __name__ == "__main__":
    seed_accounts()
