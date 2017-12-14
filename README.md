# YAML save/load storage for Errbot

## About

This is Errbot storage plugin that manage persistent variables on local YAML file by [PyYAML](http://pyyaml.org/wiki/PyYAML).

## Usage

1. Install PyYAML
2. Edit config.py to use this plugin

```python
BOT_EXTRA_STORAGE_PLUGINS_DIR = '/path/to/storage-plugins'
STORAGE = 'YAML'
```

3. Run errbot by `errbot -T`

## Caution

This plugin implement for debug in localhost. So it save YAML file each time varibales be modified.
You should not use in production environment.
