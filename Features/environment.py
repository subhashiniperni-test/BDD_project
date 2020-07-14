from selenium.webdriver import Chrome


def before_all(context):
    path = "C:\DdriveData\downloads\chromedriver_win32\chromedriver.exe"
    context.driver = Chrome(executable_path=path)


def after_all(context):
    context.driver.close()
