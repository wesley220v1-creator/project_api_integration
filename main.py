import time
import logging
from src.config import Settings
from src.sync_manager import SyncManager

logging.basicConfig(level=Settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    sync = SyncManager(Settings.BASE_TRELLO_BOARD_ID, Settings.BASE_ASANA_PROJECT_ID)
    
    try:
        while True:
            logger.info("Starting synchronization cycle")
            sync.sync_once()
            logger.info("Cycle finished, sleeping %s seconds", Settings.POLL_INTERVAL_SECONDS)
            time.sleep(Settings.POLL_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        logger.info("Stopped by user")
