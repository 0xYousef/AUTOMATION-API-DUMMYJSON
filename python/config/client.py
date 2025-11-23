import json
from .APIConfig import APIConfig
from .envirment import Environment


class Client:
    def __init__(self, env:Environment):
        self.env = env
        self.routes = self._load_routes()

    def _load_routes(self) -> APIConfig :
        with open("resources/routes.json", "r") as f:
            data = json.load(f)
        return APIConfig(data)
