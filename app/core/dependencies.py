import logging

# Configuration de base
logging.basicConfig(
    level=logging.INFO,  # Niveau de log minimal (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Affiche les logs dans la console
    ],
)

logger = logging.getLogger("my_app")