from config.envirment import Environment
from config.client import Client
from core.apis.AuthAPI import AuthAPI
from core.dto.AuthForm import AuthForm
from core.dto.RefreshTokenForm import RefreshTokenForm

env = Environment("dev")
client = Client(env)
auth = AuthAPI(client)
authForm = AuthForm()

authForm.username = "michaelw"
authForm.password = "michaelwpass"
authForm.expired = 60

res = auth.login(authForm)
print(res.status_code)
print(res.json()["firstName"])
print(client.env.get("accessToken"))

refreshTokenForm = RefreshTokenForm()
refreshTokenForm.refreshToken = client.env.get("refreshToken")
refreshTokenForm.expired = 30
res2 = auth.refreshToken(client.env.get("refreshToken"))
print(res2.status_code)
print(res2.json())
