from config.envirment import Environment
from config.client import Client
from core.apis.AuthAPI import AuthAPI

env = Environment("dev")
client = Client(env)
auth = AuthAPI(client)

res = auth.login("michaelw", "michaelwpass")
print(res.status_code)
print(res.json()["firstName"])
print(client.env.get("accessToken"))

res2 = auth.refreshToken(client.env.get("refreshToken"))
print(res2.status_code)
print(res2.json())
