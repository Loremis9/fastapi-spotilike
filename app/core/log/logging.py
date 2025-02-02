import logging.config
# Charger le fichier de configuration
logging.config.fileConfig('app/core/log/logging.conf')

# Utiliser les logs
logger = logging.getLogger("uvicorn")

def log_error_console(message: str):
    logger.error(message)


def log_info_console(message : str):
    logger.info(message)
