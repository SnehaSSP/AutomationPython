import pytest
import logging
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'Selenium Pytest Login'
        config.stash[metadata_key]['Module Name'] = 'Login Tests'
        config.stash[metadata_key]['Tester'] = 'Sneha'
