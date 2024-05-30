import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.types import Action, AuthFunction, Schema
from ckan.common import CKANConfig
import ckan.plugins.toolkit as tk
from typing import Dict
from .logic.actions import (
    cudc_import_configs_get,
    cudc_import_config_delete,
    cudc_import_config_update,
    cudc_import_run,
    cudc_import_logs_get,
    cudc_import_log_delete,
)

log = logging.getLogger(__name__)


class UdcImportOtherPortalsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IActions)

    def configure(self, config: CKANConfig):
        log.info("Udc ImportOtherPortals Plugin Loaded!")

    # IActions
    def get_actions(self) -> Dict[str, Action]:
        return {
            "cudc_import_configs_get": cudc_import_configs_get,
            "cudc_import_config_update": cudc_import_config_update,
            "cudc_import_run": cudc_import_run,
            "cudc_import_config_delete": cudc_import_config_delete,
            "cudc_import_logs_get": cudc_import_logs_get,
            "cudc_import_log_delete": cudc_import_log_delete,
        }
