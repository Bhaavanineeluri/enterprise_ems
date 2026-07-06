from utils.jwt_handler import create_access_token, create_refresh_token


def generate_tokens(user):

    access_token = create_access_token(
        {
            "sub": user.email,
            "role": user.role
        }
    )

    refresh_token = create_refresh_token(
        {
            "sub": user.email
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