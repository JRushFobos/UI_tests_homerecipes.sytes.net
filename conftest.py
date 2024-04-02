import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def driver():
    options = webdriver.ChromeOptions()
    driver_service = Service(ChromeDriverManager(driver_version="123.0.6312.58").install())
    # driver_service = Service(ChromeDriverManager(driver_version="114.0.5735.90").install())
    # driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
