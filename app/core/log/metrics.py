from prometheus_client import Counter
from .logging import log_error_console, log_info_console


error_counter_metric = Counter("server_errors", "Nombre d'erreurs du serveur", ["error_tag"])
info_counter_metric = Counter("server_info", "Informations sur actions effectuées", ["info_tag"])

def log_error_with_metrics(message, status_http= '200'):
    log_error_console(f'{message}, {status_http}')
    error_counter_metric.labels(error_tag=f'{message},{status_http}').inc(1)

def log_info(message, status_http='200'):
    log_info_console(f'{message}, {status_http}')
    info_counter_metric.labels(info_tag=f'{message},{status_http}').inc(1)
