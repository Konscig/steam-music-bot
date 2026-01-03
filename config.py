import dotenv, os

class Config():
    """
    Класс конфигурации бота. Здесь можно задать пользователя, через которого подлкючится бот к Steam, а также ключ API
    """
    def __init__(self):
        self.env = dotenv.load_dotenv("./.env")
    
    def get_user(self) -> dict[str, str]:
        """Возвращает словарь с данными о пользователе

        Returns:
            user: словарь с данными о пользователе
        """
        user = {"username": os.getenv("USER"),
                "password": os.getenv("PASSWORD")}
        return user
    
    def get_api(self) -> str:
        """Возвращает строку содержащую API ключ

        Returns:
            str: API ключ
        """
        api = os.getenv("API_KEY")
        return api
    