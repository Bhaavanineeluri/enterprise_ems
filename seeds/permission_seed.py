from sqlalchemy.orm import Session

from database import SessionLocal

from models.role import Role
from models.permission import Permission
from models.resource import Resource
from models.role_permission import RolePermission



ROLES = [
    "ADMIN",
    "EMPLOYEE",
    "CUSTOMER"
]


ACTIONS = [
    "CREATE",
    "READ",
    "UPDATE",
    "DELETE"
]


RESOURCES = [
    "COMPANY",
    "CUSTOMER",
    "PRODUCT",
    "INVENTORY"
]



def seed_permissions():

    db: Session = SessionLocal()


    try:

        # -------------------------
        # Create Roles
        # -------------------------

        roles = {}

        for role_name in ROLES:

            role = db.query(Role).filter(
                Role.name == role_name
            ).first()


            if not role:

                role = Role(
                    name=role_name
                )

                db.add(role)
                db.commit()
                db.refresh(role)


            roles[role_name] = role



        # -------------------------
        # Create Actions
        # -------------------------

        permissions = {}

        for action in ACTIONS:

            permission = db.query(Permission).filter(
                Permission.action == action
            ).first()


            if not permission:

                permission = Permission(
                    action=action
                )

                db.add(permission)
                db.commit()
                db.refresh(permission)


            permissions[action] = permission



        # -------------------------
        # Create Resources
        # -------------------------

        resources = {}

        for resource_name in RESOURCES:

            resource = db.query(Resource).filter(
                Resource.name == resource_name
            ).first()


            if not resource:

                resource = Resource(
                    name=resource_name
                )

                db.add(resource)
                db.commit()
                db.refresh(resource)


            resources[resource_name] = resource



        # -------------------------
        # ADMIN permissions
        # -------------------------

        for resource in resources.values():

            for permission in permissions.values():

                exists = db.query(RolePermission).filter(
                    RolePermission.role_id == roles["ADMIN"].id,
                    RolePermission.resource_id == resource.id,
                    RolePermission.permission_id == permission.id
                ).first()


                if not exists:

                    db.add(
                        RolePermission(
                            role_id=roles["ADMIN"].id,
                            resource_id=resource.id,
                            permission_id=permission.id
                        )
                    )



        # -------------------------
        # EMPLOYEE permissions
        # -------------------------

        employee_permissions = [
            ("PRODUCT","READ"),
            ("PRODUCT","UPDATE"),
            ("INVENTORY","READ"),
            ("INVENTORY","UPDATE"),
        ]


        for resource_name, action in employee_permissions:

            db.add(
                RolePermission(
                    role_id=roles["EMPLOYEE"].id,
                    resource_id=resources[resource_name].id,
                    permission_id=permissions[action].id
                )
            )



        # -------------------------
        # CUSTOMER permissions
        # -------------------------

        customer_permissions = [
            ("CUSTOMER","READ")
        ]


        for resource_name, action in customer_permissions:

            db.add(
                RolePermission(
                    role_id=roles["CUSTOMER"].id,
                    resource_id=resources[resource_name].id,
                    permission_id=permissions[action].id
                )
            )


        db.commit()


        print("Permission seed completed")


    except Exception as e:

        db.rollback()

        print(
            "Seed failed:",
            e
        )


    finally:

        db.close()



if __name__ == "__main__":

    seed_permissions()