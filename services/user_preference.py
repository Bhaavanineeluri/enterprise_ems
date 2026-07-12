from sqlalchemy.orm import Session

from repositories.user_preference import (
    user_preference_repository
)

from models.user_preference import UserPreference


def get_my_preferences(
    db: Session,
    current_user
):

    preference = user_preference_repository.first_by(
        db,
        user_id=current_user.id
    )

    if not preference:

        preference = UserPreference(
            user_id=current_user.id
        )

        user_preference_repository.create(
            db,
            preference
        )

    return preference


def update_my_preferences(
    db: Session,
    current_user,
    data
):

    preference = user_preference_repository.first_by(
        db,
        user_id=current_user.id
    )

    if not preference:

        preference = UserPreference(
            user_id=current_user.id
        )

        user_preference_repository.create(
            db,
            preference
        )

    update_data = data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            preference,
            key,
            value
        )

    return user_preference_repository.update(
        db,
        preference
    )