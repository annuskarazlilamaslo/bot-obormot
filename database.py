import json
import logging
import config

logger = logging.getLogger(__name__)


def _load_settings():
    """Вспомогательная функция для безопасного чтения настроек."""

    if not config.SETTINGS_FILE.exists():
        return {}
    try:
        with open(
            config.SETTINGS_FILE, "r", encoding=config.ENCODING
        ) as settings_file:
            return json.load(settings_file)
    except Exception:
        logger.exception("Критическая ошибка при чтении файла настроек:")
        return {}


def get_welcome_channel(guild_id):
    """Получает ID канала приветствий для конкретного сервера."""

    data = _load_settings()
    return data.get(str(guild_id), {}).get("welcome_channel", 0)


def save_welcome_channel(guild_id, channel_id):
    """Сохраняет ID канала приветствий для конкретного сервера."""

    data = _load_settings()

    data.setdefault(str(guild_id), {})["welcome_channel"] = channel_id

    try:
        with open(
            config.SETTINGS_FILE, "w", encoding=config.ENCODING
        ) as settings_file:
            json.dump(data, settings_file, indent=4, ensure_ascii=False)
    except Exception:
        logger.exception(
            f"Критическая ошибка при записи настроек для сервера {guild_id}:"
        )

