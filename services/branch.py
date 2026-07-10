from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.branch import BranchCreate

from core.unit_of_work.uow import UnitOfWork



def create_branch(
    db: Session,
    data: BranchCreate
):

    uow = UnitOfWork(db)



    company = uow.companies.get(
        db,
        data.company_id
    )


    if not company:

        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )



    existing = uow.branches.first_by(
        db,
        branch_code=data.branch_code
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="Branch code already exists"
        )



    try:

        branch = uow.branches.model(
            **data.model_dump()
        )


        uow.branches.create(
            db,
            branch
        )


        uow.commit()

        uow.refresh(branch)


        return branch



    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Branch creation failed: {str(e)}"
        )




def get_all_branches(db:Session):

    uow = UnitOfWork(db)

    return uow.branches.get_all(db)




def get_branch(
    db:Session,
    branch_id:int
):

    uow = UnitOfWork(db)

    branch = uow.branches.get(
        db,
        branch_id
    )


    if not branch:

        raise HTTPException(
            status_code=404,
            detail="Branch not found"
        )


    return branch
# =====================================================
# DELETE BRANCH
# =====================================================

def delete_branch(
    db: Session,
    branch_id: int
):

    uow = UnitOfWork(db)

    branch = uow.branches.get(
        db,
        branch_id
    )

    if not branch:

        raise HTTPException(
            status_code=404,
            detail="Branch not found"
        )

    try:

        uow.branches.delete(
            db,
            branch
        )

        uow.commit()

        return {
            "success": True,
            "message": "Branch deleted successfully"
        }

    except Exception as e:

        uow.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )