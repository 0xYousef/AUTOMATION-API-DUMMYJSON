class AuthForm:
    def __init__(self):
        self.__username: str = ""
        self.__password: str = ""
        self.__expired: int = 60
    
    @property
    def username(self) -> str:
        """Get the username."""
        return self.__username
    
    @username.setter
    def username(self, value: str) -> None:
        """Set the username with validation."""
        if not isinstance(value, str):
            raise ValueError("Username must be a string")
        self.__username = value.strip()
    
    @property
    def password(self) -> str:
        """Get the password."""
        return self.__password
    
    @password.setter
    def password(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Password must be a string")
        self.__password = value
    
    @property
    def expired(self) -> int:
        return self.__expired
    
    @expired.setter
    def expiresInMins(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Expires in minutes must be an integer")
        if value <= 0:
            raise ValueError("Expires in minutes must be greater than 0")
        self.__expired = value
    
    def clear(self) -> None:
        self.__username = ""
        self.__password = ""
        self.__expired = 60
    
    def __str__(self) -> str:
        return f"AuthForm(username='{self.__username}', has_password={bool(self.__password)})"
    
    def to_dict(self) -> dict:
        return {
            "username": self.__username,
            "password": self.__password,
            "expiresInMins": self.__expired
        }