import bcrypt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_salt() -> str:
    return bcrypt.gensalt().decode("utf-8")

def verify_password(plain: str, hash: str) -> bool:
    return pwd_context.verify(plain, hash)

def get_password_hash(plain: str) -> str:
    return pwd_context.hash(plain)