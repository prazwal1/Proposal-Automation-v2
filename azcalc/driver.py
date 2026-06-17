"""Chrome webdriver factory for the v2 agent (standalone, does not touch v1)."""
import os
import tempfile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CALCULATOR_URL = "https://azure.microsoft.com/en-us/pricing/calculator/"


def get_driver(download_path=None, headless=False):
    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")

    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-notifications")

    # Containers run as root with a tiny /dev/shm; both flags are required there
    # and harmless on the desktop. Opt-in via env so desktop runs are unchanged.
    if os.environ.get("CHROME_NO_SANDBOX"):
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    # In Docker we ship a pinned Chromium + matching driver instead of letting
    # webdriver-manager download one; point Selenium at them via env.
    chrome_bin = os.environ.get("CHROME_BIN")
    if chrome_bin:
        chrome_options.binary_location = chrome_bin

    download_dir = os.path.abspath(download_path) if download_path else tempfile.gettempdir()
    os.makedirs(download_dir, exist_ok=True)
    if os.name == "nt":
        download_dir = os.path.normpath(download_dir)

    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": False,
            "safebrowsing.disable_download_protection": True,
            "profile.default_content_settings.popups": 0,
        },
    )

    driver_path = os.environ.get("CHROMEDRIVER_PATH")
    service = Service(driver_path) if driver_path else Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    if not headless:
        driver.maximize_window()
    return driver
