class AuthForm:
    def __init__(self):
        self.__username: str = ""
        self.__password: str = ""
    
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
    
    def clear(self) -> None:
        self.__username = ""
        self.__password = ""
    
    def __str__(self) -> str:
        return f"AuthForm(username='{self.__username}', has_password={bool(self.__password)})"
    
    def to_dict(self) -> dict:
        return {
            "username": self.__username,
            "password": self.__password
        }

if __name__ == '__main__':
    auth_form = AuthForm()
    
    auth_form.username = "john_doe"
    auth_form.password = "secure_password"
    
    print("Username:", auth_form.username)
    print("Password:", auth_form.password)
    
    print("String representation:", str(auth_form))
    
    print("Dictionary representation:", auth_form.to_dict())
    
    try:
        auth_form.username = 123  # This should raise ValueError
    except ValueError as e:
        print("Validation error:", e)
    
    auth_form.clear()
    print("After clear - Username:", auth_form.username)
    print("After clear - Password:", auth_form.password)