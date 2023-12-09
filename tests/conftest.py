import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service_obj = Service("/Users/ADMIN/PycharmProjects/GreencartFK/drivers/chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=service_obj)

    elif browser_name == "firefox":
        #driver = webdriver.Firefox(executable_path=GeckoDriverManager().download_and_install())
        service_obj = Service("/Users/ADMIN/PycharmProjects/GreencartFK/drivers/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)

    elif browser_name == "edge":
        print("edge driver starts")
        #driver = webdriver.Edge(executable_path=EdgeDriverManager().install())
        service_obj = Service("/Users/ADMIN/PycharmProjects/GreencartFK/drivers/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    #driver.close()
