import csv
from database import Base, engine, SessionLocal
from models import Account

Base.metadata.create_all(bind=engine)

def seed_accounts():
    db = SessionLocal()

    with open("bankserver.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # prevent duplicate VPAs
            if db.query(Account).filter(Account.vpa == row["VPA"]).first():
                continue

            account = Account(
                vpa=row["VPA"].strip(),
                name=row["name"].strip(),
                mid=int(float(row["MID"])) if row.get("MID") else None,
                mcc=int(row["MCC"]) if row.get("MCC") else None,
                geohash=row.get("geohash") or None,
                fraud_reports=int(row["flags"]) if row.get("flags") else 0
            )
            db.add(account)

    db.commit()
    db.close()
    print("✅ Database seeded successfully")

if __name__ == "__main__":
    seed_accounts()
