from database import engine, SessionLocal
from models import Base, Account

Base.metadata.create_all(bind=engine)

db = SessionLocal()

accounts = [
    Account(
        vpa="rahul123@oksbi",
        acc_holder_name="Rahul",
        account_type="PERSONAL",
        mcc=None,
        kyc_status="LOW",
        geohash=None,
        account_age_days=30,
        status="ACTIVE"
    ),
    Account(
        vpa="ganeshtea@okaxis",
        acc_holder_name="Ganesh Tea Stall",
        account_type="MERCHANT",
        mcc="5812",
        kyc_status="FULL",
        geohash="te7x8hjn6f",
        account_age_days=900,
        status="ACTIVE"
    ),
    Account(
        vpa="karan@okaxis",
        acc_holder_name="Karan",
        account_type="PERSONAL",
        mcc=None,
        kyc_status="FULL",
        geohash=None,
        account_age_days=600,
        status="ACTIVE"
    ),
    Account(
            vpa="paytmqr56924@icici",
            acc_holder_name="TechOn Electronics",
            account_type="MERCHANT",
            mcc=8828,
            kyc_status="FULL",
            geohash="te7utkex6g",
            account_age_days=600,
            status="ACTIVE"
    ),
    Account(
            vpa="paytmqr56925@icici",
            acc_holder_name="Rakesh Kirana Store",
            account_type="MERCHANT",
            mcc=8928,
            kyc_status="FULL",
            geohash="gpdr8b52g4",
            account_age_days=600,
            status="ACTIVE"
    )
]

db.add_all(accounts)
db.commit()
db.close()

print("Reference account database initialized.")
