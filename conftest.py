import pytest
import shutil
import os
from selenium import webdriver
from config import URLS

# Фикстура для драйвера
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URLS.URL_MAIN)
    yield driver
    driver.quit()

# Хук для очистки allure_results
def pytest_sessionstart(session):
    """Очистка папки allure_results перед запуском тестов."""
    results_dir = "allure_results"
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    os.makedirs(results_dir)
