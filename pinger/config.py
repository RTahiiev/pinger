from dotenv import dotenv_values


class Config:
    """
    Configuration class
    """
    config = dotenv_values(".env")

    URL = config.get("URL", None)
    EMAIL = config.get("EMAIL", None)
    PASSWORD = config.get("PASSWORD", None)
