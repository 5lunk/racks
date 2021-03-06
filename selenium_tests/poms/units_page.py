from locators import Locators


class UnitsPage():

    def __init__(self, driver):
        self.driver = driver
        self.first_device_loc = Locators.first_device_loc
        self.second_device_loc = Locators.second_device_loc
        self.first_device_loc = Locators.first_device_loc
        self.first_device_loc = Locators.first_device_loc
        self.second_device_loc = Locators.second_device_loc
        self.add_device_button_xpath = Locators.add_device_button_xpath

    def open_first_device(self):
        self.driver.find_element_by_xpath(self.first_device_loc).click()

    def open_second_device(self):
        self.driver.find_element_by_xpath(self.second_device_loc).click()

    def get_first_device_loc(self):
        return self.driver.find_element_by_xpath(self.first_device_loc)

    def get_second_device_loc(self):
        return self.driver.find_element_by_xpath(self.second_device_loc)

    def add_new_device(self):
        self.driver.find_element_by_xpath(self.add_device_button_xpath).click()