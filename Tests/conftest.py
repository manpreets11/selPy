import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service)
    if request.param == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=service)
    if request.param == "edge":
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        web_driver = webdriver.Edge(service=service)
    request.cls.driver = web_driver
    yield
    web_driver.close()

