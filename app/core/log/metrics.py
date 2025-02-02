from prometheus_client import Counter
from .logging import log_error_console, log_info_console
from typing import Union
error_counter = Counter("server_errors", "Nombre d'erreurs du serveur", ["error_tag"])
info_counter = Counter("server_info", "informations sur actions effectue", ["info_tag"])

def log_error_with_metrics(tag: Union[str,list[str]]):
    if isinstance(tag,list):
        log_error_console(','.join(tag))
        return
    log_error_console(tag)
    error_counter.labels(error_tag=tag).inc()
    return

def log_info(tag: Union[str,list[str]]):
    if  isinstance( tag,list):
        log_info_console(','.join(tag))
    log_info_console(tag)
    info_counter.labels(info_tag=tag).inc()
    return

