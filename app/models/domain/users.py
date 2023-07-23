from typing import Optional
from app.models.comon import DateTimeModelMixin, IDModelMixin
from app.models.domain.rwmodel import RWModel
from app.services import security

class User(RWmodel):
    username: str
    email: str
    image: Optional[str] = None

class UserInDB(IDModelMixin, DateTimeModelMixin, User):
    salt: str = ""
    hashed_pass: str = ""

    def check_pass(self, password: str) -> bool:
        return security.verify_password(password + self.salt, self.hashed_pass)

    def change_pass(self, password: str) -> None:
        self.salt = security.generate_salt()
        self.hashed_pass = security.get_password_hash(self.salt + password)
