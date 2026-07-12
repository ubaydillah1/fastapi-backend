from fastapi import HTTPException, status

from app.repositories.user import UserRepository
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.utils.security import create_access_token, hash_password, verify_password


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, payload: RegisterRequest) -> TokenResponse:
        existing_user = self.repository.get_by_email(str(payload.email))
        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        user = self.repository.create_auth_user(
            email=str(payload.email),
            password=hash_password(payload.password),
            name=payload.name,
            age=payload.age,
        )
        return self._create_token_response(str(user.id))

    def login(self, payload: LoginRequest) -> TokenResponse:
        user = self.repository.get_by_email(str(payload.email))
        
        if user is None or not verify_password(payload.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        return self._create_token_response(str(user.id))

    def _create_token_response(self, user_id: str) -> TokenResponse:
        token = create_access_token({"sub": user_id})
        return TokenResponse(access_token=token)
