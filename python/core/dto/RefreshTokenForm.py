class RefreshTokenForm:
    def __init__(self):
        self.__refreshToken: str = ""
        self.__expired: int = 60
    
    @property
    def refreshToken(self) -> str:
        return self.__refreshToken
    
    @refreshToken.setter
    def refreshToken(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Refresh token must be a string")
        self.__refreshToken = value
    
    @property
    def expired(self) -> int:
        return self.__expired
    
    @expired.setter
    def expired(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Expires in minutes must be an integer")
        if value <= 0:
            raise ValueError("Expires in minutes must be greater than 0")
        self.__expired = value
    
    def clear(self) -> None:
        self.__refreshToken = ""
        self.__expired = 60
    
    def to_dict(self) -> dict:
        return {
            "refreshToken": self.__refreshToken,
            "expiresInMins": self.__expired
        }