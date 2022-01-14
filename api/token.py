import json

from O365 import Account
from O365 import FileSystemTokenBackend

from config import Config


def get_token():
    """
    認証用tokenを取得する

    """
    config = Config()
    credentials = (config.client_id, config.client_secret)
    token_backend = \
        FileSystemTokenBackend(
            token_path=config.token_path,
            token_filename=config.token_file
        )
    account = Account(credentials, token_backend=token_backend)
    if account.authenticate(scopes=['basic', 'sharepoint', 'sharepoint_dl']):
        print('Authenticated!')
    # ファイル出力
    token = token_backend.get_token()
    with open(
        '{}/{}'.format(config.token_path, config.token_file),
        mode='w',
        encoding='utf-8'
    ) as f:
        json.dump(
            dict(token),
            f,
            ensure_ascii=False,
            indent=2
        )
