import json
from time import sleep
from typing import List
from hamcrest import *

import pytest
from addict import Dict

from selene.support.shared import browser
from selene import by, be, have

customer_name_elem = browser.element(by.name('custname'))
customer_tele_elem = browser.element(by.name('custtel'))
customer_email_elem = browser.element(by.name("custemail"))

preferred_delivery_time = browser.element(by.name('delivery'))
delivery_instructions = browser.element(by.name("comments"))

submit_button = browser.element(by.xpath("//button[text()='Submit order']"))


def select_pizza_size(size: str) -> browser.element:
    return browser.element(by.xpath(f".//input[@value ='{size}']"))


def select_pizza_toppings(topping: str) -> browser.element:
    return browser.element(by.xpath(f".//input[@value = '{topping}' ]"))


@pytest.mark.parametrize('scenario', [
    Dict(name="saji", phone=524281482, email="saji.tibi@gmail.com", size="medium", toppings=["bacon", "onion"],
         time=1700, comments="some comment")])
def test_1(scenario):
    browser.open('https://httpbin.org/forms/post')
    customer_name_elem.type(scenario.name)
    customer_tele_elem.type(scenario.phone)
    customer_email_elem.type(scenario.email)
    select_pizza_size(scenario.size).click()
    for topping in scenario.toppings:
        select_pizza_toppings(topping).click()
    preferred_delivery_time.type(scenario.time)
    delivery_instructions.type(scenario.comments)
    submit_button.click()
    data = json.loads(browser.elements(by.xpath(".//body/pre"))[0].text)

    assert_order_info(scenario,data["form"])


def assert_order_info(scenario,data):
    print(scenario)
    for key in data:
        print(data)
        print(scenario.key)
        assert data[key] == scenario.key
        assert_that(data[key], equal_to(scenario.key), 'Value is match to expected one')
