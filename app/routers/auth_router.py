from fastapi import APIRouter, Depends, status

from app.controllers.auth_controller import login, register
from app.dependencies.auth import get_auth_service
from app.schemas.auth import AuthResponse, LoginRequest, RegisterRequest
from app.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_route(
    payload: RegisterRequest,
    service: AuthService = Depends(get_auth_service),
):
    return register(payload, service)


@router.post("/login", response_model=AuthResponse)
def login_route(
    payload: LoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    return login(payload, service)
