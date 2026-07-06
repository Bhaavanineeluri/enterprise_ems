from database import SessionLocal
from models.role import Role
from models.permission import Permission


db = SessionLocal()

roles = ["ADMIN", "EMPLOYEE", "CUSTOMER", "MANAGER"]

permissions = [
    {"name": "View Users", "code": "view_users"},
    {"name": "Create Users", "code": "create_users"},
    {"name": "Delete Users", "code": "delete_users"},
    {"name": "View Reports", "code": "view_reports"},
]

for r in roles:
    exists = db.query(Role).filter(Role.name == r).first()
    if not exists:
        db.add(Role(name=r))

for p in permissions:
    exists = db.query(Permission).filter(Permission.code == p["code"]).first()
    if not exists:
        db.add(Permission(**p))

db.commit()
db.close()

print("RBAC seed completed")