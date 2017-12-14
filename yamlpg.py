import os
import yaml
from typing import Any, Iterable
from errbot.storage.base import StorageBase, StoragePluginBase


class YAMLStorage(StorageBase):
    def __init__(self, save_path):
        self.save_path = save_path
        try:
            with open(self.save_path) as fp:
                self.data = yaml.safe_load(fp)
        except FileNotFoundError:
            self.data = {}

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value
        self.close()

    def get(self, key: str) -> Any:
        return self.data[key]

    def remove(self, key: str) -> None:
        del self.data[key]
        self.close()

    def len(self) -> int:
        keys = self.keys()
        return len(keys)

    def keys(self) -> Iterable[str]:
        return self.data.keys()

    def close(self) -> None:
        with open(self.save_path, 'w') as fp:
            yaml.safe_dump(
                self.data, fp, encoding='utf-8', allow_unicode=True, default_flow_style=False)


class YAMLPlugin(StoragePluginBase):
    def __init__(self, bot_config):
        super().__init__(bot_config)
        self.data_dir = bot_config.BOT_DATA_DIR

    def open(self, namespace: str) -> StorageBase:
        save_path = os.path.join(self.data_dir, f"{namespace}.yml")
        return YAMLStorage(save_path)
