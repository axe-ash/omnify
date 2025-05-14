from behave import given, when, then
from selenium import webdriver
from pages.hotel_booking_page import HotelBookingPage
import time

@given("I open the hotel booking application")
def step_open_app(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://example.com/hotel-booking")
    context.page = HotelBookingPage(context.driver)

@when('I search for hotels in "{city}" from "{check_in}" to "{check_out}"')
def step_search_hotels(context, city, check_in, check_out):
    context.page.search_hotels(city, check_in, check_out)

@when("I select the first hotel from the search results")
def step_select_first_hotel(context):
    context.page.select_first_hotel()

@when('I apply the coupon code "{coupon_code}"')
def step_apply_coupon(context, coupon_code):
    context.page.apply_coupon(coupon_code)

@then("I should see the discount applied correctly")
def step_verify_discount(context):
    assert context.page.is_discount_applied(), "Discount was not applied correctly"

@then("I proceed to checkout without completing payment")
def step_checkout(context):
    context.page.proceed_to_checkout()
    time.sleep(2)
    context.driver.quit()
