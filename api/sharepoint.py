from O365 import Account
from O365 import FileSystemTokenBackend
import pandas as pd

from config import Config


config = Config()


def get_sharepoint():
    credentials = (config.client_id, config.client_secret)
    token_backend = \
        FileSystemTokenBackend(
            token_path=config.token_path,
            token_filename=config.token_file
        )
    account = Account(credentials, token_backend=token_backend)
    return account.sharepoint()


def get_list_records():
    sharepoint = get_sharepoint()
    # サイトの取得
    site = \
        sharepoint.get_site('root', config.site_collection_id, config.site_id)

    result_dict = dict()
    for list_id in config.list_ids:
        # リストを取得
        target_list = site.get_list_by_name(list_id)
        # レコードを取得
        records = target_list.get_items(expand_fields=True)
        # pandasに変換
        records_df = pd.DataFrame([record.fields for record in records])
        # 辞書として保持
        result_dict[list_id] = records_df

    return result_dict
