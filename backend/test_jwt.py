from backend.security.auth import (
    create_access_token
)

token = create_access_token(
    {
        "sub": "lalitha",
        "role": "admin"
    }
)

print(token)