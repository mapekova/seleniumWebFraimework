import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(
        executable_path="C:\\Users\\30018\\Desktop\\python-example\\seleniumWebFramework\\chromedriver.exe"
    )
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_login_example(driver):
    driver.get("http://localhost/litecart/admin/login.php/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name ("login").click()

