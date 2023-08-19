import dotenv

from src.bot import Bot
from src.server import server

dotenv.load_dotenv()


def main():
    bot = Bot()
    bot.daemon = True
    bot.start()
    server.start_server()


if __name__ == "__main__":
    main()
