from config.client import Client
class UsersAPI:
    def __init__(self,client:Client):
        self.__url = client.env.get()

    def view_all(self):
        pass

