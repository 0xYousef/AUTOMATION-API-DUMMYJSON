from config.client import Client
import requests
from requests import Response
from core.dto.AuthForm import AuthForm
from core.dto.RefreshTokenForm import RefreshTokenForm

class AuthAPI:

    def __init__(self, client: Client):
      self.env = client.env
      self.routes = client.routes.auth
      self.root = self.env.root + self.routes.base

    def login(self, authForm: AuthForm) -> Response:
      url = self.root + self.routes.routes.login

      print(f"[AuthAPI] Login using user={authForm.username}")
      print(f"URL = {url}")

      response = requests.post(url, json=authForm.to_dict())
      data = response.json()
      self.env.set("access-token", data["accessToken"])
      self.env.set("refresh-token",data["refreshToken"])
      self.env.set("expired-token",authForm.expired)
      return response

    def refreshToken(self,refreshTokenForm: RefreshTokenForm) -> Response:
      url = self.root + self.routes.routes.refresh
      response = requests.post(url, json=refreshTokenForm.to_dict())
      data = response.json()
      if "accessToken" in data:
          self.env.set("accessToken", data["accessToken"])
      return response
