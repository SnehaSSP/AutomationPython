import pytest
import csv
import logging

from LoginAutomation22May.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_login(driver):
    login_page = LoginPage(driver)
    logger.info("opening and maximizing browser")
    login_page.open_browser()
    logger.info("entering credentials")
    login_page.login()
    logger.info("Verifying login")
    assert "The Internet" in driver.title
