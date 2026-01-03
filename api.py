from steam.client import SteamClient
from config import Config

client = SteamClient()
config = Config()

user = config.get_user()
api = config.get_api()

client.cli_login(
    username=user["username"],
    password=user["password"]
)


