import os
from boxsdk import Client, OAuth2

auth = OAuth2(
    client_id="y1901t01zae4h31afuvk30fsk3za3t74",
    client_secret="Cj6XBeBLAwWWTlDE4rYXUVsmkJdmmj4x",
    access_token="XKrgihAb7861FGheHHJogLQz0naofgvF",
)

client = Client(auth)

# ユーザー情報を取得
user = client.user().get()
print("User Login: ", user["login"])


def download_folder(client, folder_id, local_folder_path):
    """
    指定したBoxフォルダからファイルとサブフォルダを再帰的にダウンロードする
    """
    folder = client.folder(folder_id).get()
    items = folder.get_items()
    for item in items:
        if item.type == "file":
            download_file(item, local_folder_path)
        elif item.type == "folder":
            new_folder_path = os.path.join(local_folder_path, item.name)
            os.makedirs(new_folder_path, exist_ok=True)
            download_folder(client, item.id, new_folder_path)


def download_file(file_item, local_folder_path):
    """
    Boxファイルをローカルにダウンロードする
    """
    local_file_path = os.path.join(local_folder_path, file_item.name)
    if os.path.exists(local_file_path):
        print(f"File already exists {local_file_path}")
        return
    with open(local_file_path, "wb") as file_output:
        file_item.download_to(file_output)
    print(f"Downloaded file to {local_file_path}")


# ダウンロードを開始するフォルダIDと保存先のローカルパス
folder_id_to_download = "245311281590"
# folder_id_to_download = "c2hc5oextdsjvczptotllx76hzf0tfln"
local_save_path = "data/"


if not os.path.exists(local_save_path):
    os.mkdir(local_save_path)

# ダウンロードプロセスを開始
download_folder(client, folder_id_to_download, local_save_path)
