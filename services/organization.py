from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.company import Company


def get_company_hierarchy(
    db: Session,
    company_id: int
):

    company = (
        db.query(Company)
        .filter(
            Company.id == company_id
        )
        .first()
    )

    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return {
        "company": {
            "id": company.id,
            "name": company.company_name,
            "code": company.company_code,
            "branches": [
                {
                    "id": branch.id,
                    "name": branch.branch_name,
                    "departments": [
                        {
                            "id": department.id,
                            "name": department.department_name,
                            "teams": [
                                {
                                    "id": team.id,
                                    "name": team.team_name
                                }
                                for team in department.teams
                            ]
                        }
                        for department in branch.departments
                    ]
                }
                for branch in company.branches
            ]
        }
    }