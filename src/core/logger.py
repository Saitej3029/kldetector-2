import logging
import os

# Create logs directory if it doesn't exist
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_directory, 'edr_log.log'))),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def log_event(message, level='info'):
    if level == 'debug':
        logger.debug(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.info(message)