from prometheus_client import Counter
from .logging import logging
error_counter = Counter("server_errors", "Nombre d'erreurs du serveur", ["error_tag"])
info_counter = Counter("server_info", "informations sur actions effectue", ["info_tag"])

def log_error_with_metrics(tag: str):
    error_counter.labels(error_tag=tag).inc()

def log_info(tag: str):
    info_counter.labels(info_tag=tag).inc()

