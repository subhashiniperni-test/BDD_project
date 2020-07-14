from behave import *
from selenium.webdriver import Chrome


@given(u'User is on registration page')
def step_impl(context):
    context.driver.get("http://www.thetestingworld.com/testings")


@when(u'User enters "username"')
def step_impl(context):
    context.driver.find_element_by_name('fld_username').send_keys("Subhashini")


@when(u'User enter password')
def step_impl(context):
    context.driver.find_element_by_name('fld_password').send_keys("Subhashini")


@when(u'User enters email')
def step_impl(context):
    context.driver.find_element_by_name('fld_email').send_keys("Subhashini@gmail.com")


@when(u'User clicks on Signup button')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@type="submit" and @value="Sign up"]').click()


@then(u'User should get registered')
def step_impl(context):
    print("User registered succesfully")


@when(u'User enters username')
def step_impl(context):
    context.driver.find_element_by_name('fld_username').send_keys("Subhashini")


@then(u'User should not get registered')
def step_impl(context):
    print("User not registered")
