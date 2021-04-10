import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(
        executable_path="C:\\Users\\30018\\Desktop\\python-example\\seleniumWebFramework\\chromedriver.exe"
    )
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("q")
    # driver.FindElement(By.NAME("q")).SendKeys(Keys.RETURN)
    driver.find_element_by_xpath("//div[@class='FPdoLc tfB0Bf']/center/input[@class='gNO89b']").send_keys(Keys.RETURN)
    # wait.Until(ExpectedConditions.TitleIs("Football- Поиск в Google"))
    # WebDriverWait(driver, 10).until(EC.title_is("Webdriver - Поиск в Google"))





