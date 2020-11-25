# -*- coding: utf-8 -*

import unittest
import pytest
import logging
import os
from base.webdriverfactory import WebDriverFactory
from helpers.data_helper import get_test_data
from helpers.config_helper import get_config_data
from .globalvar import get_global_value

LOGGER = logging.getLogger(__name__)


class BaseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, browser):
        self.ENV = get_global_value("ENV")
        self.BROWSER = get_global_value("BROWSER")
        self.LANGUAGE = get_global_value("LANGUAGE")

        LOGGER.info(f"ENV: {self.ENV}")
        LOGGER.info(f"BROWSER: {self.BROWSER}")
        LOGGER.info(f"LANGUAGE: {self.LANGUAGE}")

        self.test_data = get_test_data()
        self.config_data = get_config_data(ENV=self.ENV)

        self.DOMAIN = self.config_data.get("CUSTOMER_APP", "DOMAIN")
        LOGGER.info(f"DOMAIN: {self.DOMAIN}")

        # self.webdriver_factory = WebDriverFactory(browser=self.BROWSER)
        self.driver = browser
