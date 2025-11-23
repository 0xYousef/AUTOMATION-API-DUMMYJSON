import json
import os


class DotDict(dict):
    def __getattr__(self, item):
        value = self.get(item)
        if isinstance(value, dict):
            return DotDict(value)
        return value

    def __setattr__(self, key, value):
        self[key] = value

    def update(self, new_data: dict):
        for k, v in new_data.items():
            if isinstance(v, dict):
                v = DotDict(v)
            self[k] = v


class Environment:
    __ENV_DIR = "resources/env"

    def __init__(self, env_name: str = None):
        if env_name:
            self.data = self._load_env_file(env_name)
        else:
            self.data = DotDict()

    def _load_env_file(self, env_name: str) -> DotDict:
        path = f"{self.__ENV_DIR}/{env_name}.json"

        if not os.path.exists(path):
            raise FileNotFoundError(f"Environment file not found: {path}")

        with open(path, "r") as f:
            raw = json.load(f)

        return DotDict(raw)
    
    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def update(self, new_dict: dict):
        self.data.update(new_dict)

    def save(self, env_name: str):
        with open(f"{self.ENV_DIR}/{env_name}.json", "w") as f:
            json.dump(self.data, f, indent=4)

    def __getattr__(self, item):
        return getattr(self.data, item)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    @staticmethod
    def available():
        return [
            f.replace(".json", "")
            for f in os.listdir(Environment.ENV_DIR)
            if f.endswith(".json")
        ]
