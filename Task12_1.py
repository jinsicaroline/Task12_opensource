import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Task12 import LoginPage
import openpyxl


def load_test_data(filename):
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=5, values_only=True):
        data.append({
            "Test ID": row[0],
            "Username": row[1],
            "Password": row[2]
        })
    return data


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()


def test_login(driver):
    test_data = load_test_data("E:\\test_data.xlsx")
    for data in test_data:
        login_page = LoginPage(driver)
        test_id = data["Test ID"]
        username = data["Username"]
        password = data["Password"]

        print(f"Testing login with username: {username} and password: {password}")
        login_page.login(username, password)

        expected_result = "Passed" if login_page.is_login_successful() else "Failed"
        print(f"Test ID {test_id}: {expected_result}")

        # Write result to Excel or validate results
        # write_test_result("E:\\test_data.xlsx", test_id, expected_result)
        assert expected_result == "Passed", f"Test ID {test_id} failed"
