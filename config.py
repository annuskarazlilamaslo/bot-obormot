import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

ENCODING = "utf-8"
GIF_FOLDER = Path(__file__).parent / "gifs"
GIFS = list(GIF_FOLDER.glob("*.gif"))
BUTTON_TIMEOUT = 86400

GREETINGS = [
    "ОПА! В {name} летит праздничный торт! 🎂",
    "Встречайте! В {name} летит торт!",
    "Торжественная встреча {name}! ТОРТ В ЛИЦО!!!",
    "Внимание! Воздушная атака на {name}! 🎂",
    "Поприветствуем {name}! В лицо летит торт!!!",
]

SETTINGS_FILE = Path(__file__).parent / "settings.json"
