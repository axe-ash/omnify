from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HotelBookingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_hotels(self, city, check_in, check_out):
        self.wait.until(EC.element_to_be_clickable((By.ID, "city"))).send_keys(city)
        self.driver.find_element(By.ID, "checkin").send_keys(check_in)
        self.driver.find_element(By.ID, "checkout").send_keys(check_out)
        self.driver.find_element(By.ID, "searchBtn").click()

    def select_first_hotel(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".hotel-result")))
        self.driver.find_elements(By.CSS_SELECTOR, ".hotel-result")[0].click()

    def apply_coupon(self, coupon_code):
        self.wait.until(EC.presence_of_element_located((By.ID, "coupon"))).send_keys(coupon_code)
        self.driver.find_element(By.ID, "applyCoupon").click()

    def is_discount_applied(self):
        discount_text = self.wait.until(EC.visibility_of_element_located((By.ID, "discountMsg"))).text
        return "25%" in discount_text

    def proceed_to_checkout(self):
        self.driver.find_element(By.ID, "checkoutBtn").click()
