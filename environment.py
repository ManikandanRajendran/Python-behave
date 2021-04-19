import os
import shutil
import time
from selenium import webdriver


def define_browser(context, value):
    if value == "chrome":
        option = webdriver.ChromeOptions()
        context.driver = webdriver.Chrome(executable_path="./drivers/chromedriver",  chrome_options=option)
    elif value == "firefox":
        option = webdriver.FirefoxOptions()
        context.driver = webdriver.Firefox(executable_path="./drivers/geckodriver",firefox_options=option)
    else:
        value = "chrome"
        option = webdriver.ChromeOptions()
        context.driver = webdriver.Chrome(executable_path="./drivers/chromedriver", chrome_options=option)
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    print("==================================================")
    print(f"           Browser is {value}                 ")
    print("==================================================")


def define_environment(context, value):
    if value == "stage":
        context.base_url = "https://orangehrm-demo-6x.orangehrmlive.com/"
    else:
        value = "stage"
        context.base_url = "https://orangehrm-demo-6x.orangehrmlive.com/"

    print("==================================================")
    print(f"           Environment is {value}              ")
    print("==================================================")


def clear_screenshots():
    if os.path.exists('failure_screenshot/feature_errors'):
        shutil.rmtree('failure_screenshot/feature_errors')


def before_all(context):
    clear_screenshots()
    context.browser = context.config.userdata.get("browser")
    context.environment = context.config.userdata.get("environment")
    define_browser(context, context.browser)
    define_environment(context, context.environment)


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        scenario_error_dir = os.path.join('failure_screenshot', 'feature_errors')
        make_dir(scenario_error_dir)
        scenario_file_path = os.path.join(scenario_error_dir, scenario.feature.name.replace(' ', '_')
                                          + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                          + '.png')
        context.driver.save_screenshot(scenario_file_path)
    # context.driver.close()


def make_dir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
        os.makedirs(dir)


def after_all(context):
    context.driver.close()


