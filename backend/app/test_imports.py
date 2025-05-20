from app.db import Base
from app.models_db.user_orm import UserORM

print("Base metadata tables:", Base.metadata.tables.keys())
print("UserORM tablename:", UserORM.__tablename__)
