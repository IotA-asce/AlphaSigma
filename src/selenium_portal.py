"""Helpers for interacting with the remote Selenium Chrome instance.

This module connects to the Selenium server running at
``http://selenium:4444/wd/hub`` and uses a persisted Chrome profile
volume so that cookies and sessions survive container restarts.

`SeleniumPortal` exposes convenience methods to open arbitrary URLs or
perform a basic login sequence.
"""

from __future__ import annotations

from typing import Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumPortal:
    """Thin wrapper around a remote Chrome WebDriver with persisted profile."""

    def __init__(self, remote_url: str = "http://selenium:4444/wd/hub") -> None:
        options = Options()
        # Use the same user-data dir as the container's mounted profile.
        options.add_argument("--user-data-dir=/home/seluser/.config/google-chrome")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Remote(command_executor=remote_url, options=options)

    def open_url(self, url: str) -> None:
        """Navigate the browser to ``url``."""

        self.driver.get(url)

    def basic_login(
        self,
        url: str,
        username: str,
        password: str,
        username_selector: str,
        password_selector: str,
        submit_selector: str,
        wait_time: int = 10,
    ) -> None:
        """Open ``url`` and perform a simple login flow.

        The method locates fields using CSS selectors and attempts to populate
        the username and password before clicking the submit element.
        """

        self.driver.get(url)
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, username_selector))).send_keys(
            username
        )
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, password_selector))).send_keys(
            password
        )
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, submit_selector))).click()

    def close(self) -> None:
        """Close the underlying WebDriver session."""

        self.driver.quit()

    def __enter__(self) -> "SeleniumPortal":
        return self

    def __exit__(self, exc_type: Optional[type], exc: Optional[BaseException], tb) -> None:
        self.close()
