class ConfigNode:    
    def __init__(self, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self, key, ConfigNode(value))
            else:
                setattr(self, key, value)

    def __repr__(self):
        return str(self.__dict__)
    

class APIConfig:    
    def __init__(self, json_data: dict):
        self._raw = json_data 
        self._load(json_data)

    def _load(self, json_data):
        for key, value in json_data.items():
            setattr(self, key, ConfigNode(value))
