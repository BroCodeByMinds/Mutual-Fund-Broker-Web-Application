from backend.app.db import Base, engine
from backend.app.models_db.user_orm import UserORM

# This will create the tables
def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
