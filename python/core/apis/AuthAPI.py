from config.client import Client
import requests
from requests import Response

class AuthAPI:

    def __init__(self, client: Client):
      self.env = client.env
      self.routes = client.routes.auth
      self.root = self.env.root + self.routes.base

    def login(self, username: str, password: str) -> Response:
      url = self.root + self.routes.routes.login

      print(f"[AuthAPI] Login using user={username}")
      print(f"URL = {url}")

      response = requests.post(url, json={"username": username, "password": password})
      data = response.json()
      self.env.set("accessToken", data.get("accessToken"))
      self.env.set("refreshToken",data.get("refreshToken"))
      return response

    def refreshToken(self, oldRefreshToken: str) -> Response:
      url = self.root + self.routes.routes.refresh
      header = {
          "Authorization":f"Bearar {self.env.get("accessToken")}"
      }
      response = requests.post(url, json={"refreshToken": oldRefreshToken})
      data = response.json()
      if "accessToken" in data:
          self.env.set("accessToken", data["accessToken"])
      return response
