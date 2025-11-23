from .BaseAPIPage import BaseAPIPage


class AuthPage(BaseAPIPage):
    def __init__(self, client):
        super().__init__(client)
        self.node = client.routes.auth
        self.root = self._root_for(self.node)

    def login(self, username: str, password: str):
        url = self.root + self.node.routes.login
        return self.requests.post(url, json={"username": username, "password": password})

    def refresh(self, refresh_token: str):
        url = self.root + self.node.routes.refresh
        return self.requests.post(url, json={"refreshToken": refresh_token})
