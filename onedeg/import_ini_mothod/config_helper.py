# -*- coding: utf-8 -*

import os
import sys
import configparser
import logging

CURRENT_DIR = os.path.abspath(__file__)
PARENT_DIR = os.path.dirname(CURRENT_DIR)
PROJECT_DIR = os.path.dirname(PARENT_DIR)
CONFIGS_DIR = os.path.join(PROJECT_DIR, "configs")

LOGGER = logging.getLogger(__name__)


def get_config_data(ENV):
    filename = rf"{ENV}_config.ini"
    full_filename = os.path.join(CONFIGS_DIR, filename)

    try:

        if os.path.isfile(full_filename) == False:
            raise FileNotFoundError

        config_data_obj = configparser.ConfigParser(allow_no_value=True)
        config_data_obj.read(full_filename, encoding='utf8')
        return config_data_obj

    except FileNotFoundError as e:

        LOGGER.error(f"File: {full_filename} not found. Detail: {e}")
        sys.exit(1)

    except Exception as e:

        LOGGER.error(f"Read {full_filename} file occurs error. Detail: {e}")
        sys.exit(1)