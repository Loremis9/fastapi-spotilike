from prometheus_client import Counter
from .logging import log_error, log_info
from typing import Union
error_counter = Counter("server_errors", "Nombre d'erreurs du serveur", ["error_tag"])
info_counter = Counter("server_info", "informations sur actions effectue", ["info_tag"])

def log_error_with_metrics(tag: Union[str,list[str]]):
    if isinstance( tag,list):
        log_error(','.join(tag))
    log_error(tag)
    error_counter.labels(error_tag=tag).inc()

def log_info(tag: Union[str,list[str]]):
    if  isinstance( tag,list):
        log_error(','.join(tag))
    log_info(tag)
    info_counter.labels(info_tag=tag).inc()

