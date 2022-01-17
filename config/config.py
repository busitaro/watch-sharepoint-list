import configparser
import json
import os
import errno

config_file = './api.ini'


class Config():
    def __init__(self):
        if not os.path.exists(config_file):
            raise FileNotFoundError(
                errno.ENOENT,
                os.strerror(errno.ENOENT),
                config_file
            )
        self.__parser = configparser.ConfigParser()
        self.__parser.read(config_file, encoding='utf_8')

    @property
    def client_id(self):
        section = 'DEFAULT'
        key = 'client_id'
        return self.__parser.get(section, key)

    @property
    def client_secret(self):
        section = 'DEFAULT'
        key = 'client_secret'
        return self.__parser.get(section, key)

    @property
    def token_path(self):
        section = 'DEFAULT'
        key = 'token_path'
        return self.__parser.get(section, key)

    @property
    def token_file(self):
        section = 'DEFAULT'
        key = 'token_file'
        return self.__parser.get(section, key)

    @property
    def site_collection_id(self):
        section = 'DEFAULT'
        key = 'site_collection_id'
        return self.__parser.get(section, key)

    @property
    def site_id(self):
        section = 'DEFAULT'
        key = 'site_id'
        return self.__parser.get(section, key)

    @property
    def list_ids(self):
        section = 'DEFAULT'
        key = 'list_ids'
        return json.loads(self.__parser.get(section, key))
