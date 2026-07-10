from utils.jwt_handler import create_access_token, create_refresh_token




def generate_tokens(user):

    access_token = create_access_token(
        {
            "sub": user.email,
            "role": user.role,
            "company_id": user.company_id
        }
    )

    refresh_token = create_refresh_token(
        {
            "sub": user.email,
            "company_id": user.company_id
        }
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer"
    }

def logout():
    return {
        "message": "Logged out successfully"
    }