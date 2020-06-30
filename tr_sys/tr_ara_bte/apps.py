from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class BTEConfig(AppConfig):
    name = 'tr_ara_bte'

    def ready(self):
        logger.debug('### %s ready...' % self.name)
