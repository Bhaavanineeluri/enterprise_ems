from models.user import User


class PolicyEngine:

    @staticmethod
    def same_company(user: User, company_id: int):

        return user.company_id == company_id


    @staticmethod
    def is_admin(user: User):

        return user.role.name in [
            "ADMIN",
            "SUPER_ADMIN"
        ]


    @staticmethod
    def can_manage_company(
        user: User,
        company_id: int
    ):

        if PolicyEngine.is_admin(user):
            return True

        return PolicyEngine.same_company(
            user,
            company_id
        )