import logging.config
from .metrics import log_error_with_metrics, log_info
# Charger le fichier de configuration
logging.config.fileConfig('app/core/log/logging.conf')

# Utiliser les logs
logger = logging.getLogger("uvicorn")

def log_error(message: str):
    log_error_with_metrics(message)
    logger.error(message)


def log_info(message : str):
    log_info(message)
    logger.info(message)
