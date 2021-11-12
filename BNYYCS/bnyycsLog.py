
import logging;

logger = logging.getLogger(__name__);
logger.setLevel(logging.DEBUG);
_logger_ch = logging.StreamHandler();
_logger_ch.setLevel(logging.DEBUG);
_logger_formatter = logging.Formatter(
    fmt='\033[0m%(asctime)s \033[1;34m[%(levelname)s]\033[0;33m[%(name)s]\033[0m >> %(message)s',
    datefmt='%H:%M'
);
_logger_ch.setFormatter(_logger_formatter);
logger.addHandler(_logger_ch);
