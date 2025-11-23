from config.Requests import Requests


class BaseAPIPage:
    def __init__(self, client):
        self.client = client
        self.env = client.env
        self.requests = Requests

    def _root_for(self, resource_node):
        return f"{self.env.root}{resource_node.base}"

    def _auth_headers(self, extra=None):
        token = self.env.get("accessToken")
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        if extra:
            headers.update(extra)
        return headers
