import requests

class Requests:
    @staticmethod
    def post(url, json=None, headers=None):
        return requests.post(url, json=json, headers=headers)
    
    @staticmethod
    def put(url, json=None, headers=None):
        return requests.put(url, json=json, headers=headers)
    
    @staticmethod
    def patch(url, json=None, headers=None):
        return requests.patch(url, json=json, headers=headers)

    @staticmethod
    def get(url, params=None, headers=None):
        return requests.get(url, params=params, headers=headers)
    
    @staticmethod
    def delete(url,headers=None):
        return requests.delete(url=url,headers=headers)