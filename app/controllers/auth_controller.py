from app.schemas.auth import AuthResponse, LoginRequest, RegisterRequest
from app.services.auth import AuthService


def register(payload: RegisterRequest, service: AuthService) -> AuthResponse | dict:
    return {"message": "User registered successfully", "data": service.register(payload)}


def login(payload: LoginRequest, service: AuthService) -> AuthResponse | dict:
    return {"message": "User logged in successfully", "data": service.login(payload)}
