from fastapi import (APIRouter,
                     Depends,
                     Response,
                     HTTPException,
                     status,
                     Request,
                     )
from queries.accounts import Customer, CustomerIn, CustomerOut, AccountQueries
from authenticator import authenticator
from jwtdown_fastapi.authentication import Token


from pydantic import BaseModel


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: CustomerOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post("/api/accounts", response_model=AccountToken | HttpError)
async def create_account(
    info: CustomerIn,
    request: Request,
    response: Response,
    repo: AccountQueries = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        account = repo.create_customer(info, hashed_password)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = AccountForm(username=info.email, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return AccountToken(account=account, **token.dict())


@router.post("/api/accounts/login", response_model=AccountToken | HttpError)
async def login_account(
    info: AccountForm,
    request: Request,
    response: Response,
    repo: AccountQueries = Depends(),
):
    try:
        account = repo.get_one(info.username)
        if authenticator.verify_password(
            info.password, account.hashed_password
        ):
            form = AccountForm(username=info.username, password=info.password)
            token = await authenticator.login(response, request, form, repo)
            return AccountToken(account=account, **token.dict())
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )


@router.post("/api/accounts/logout")
async def logout_account(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logged out successfully"}


@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: Customer = Depends(authenticator.try_get_current_account_data),
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }


@router.get("/accounts/{email}")
def get_one(
    email: str,
    repo: AccountQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
) -> CustomerOut:
    return repo.get_one(email)


@router.get("/accounts")
def get_all(repo: AccountQueries = Depends()):
    return repo.get_all()
