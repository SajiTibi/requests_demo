from datetime import datetime, timedelta

import allure
import pytest
import requests
from addict import Dict
from hamcrest import *


@pytest.mark.parametrize('scenario', [
    Dict(params={"expr": "5+6"}, expected=11),  # 1
    Dict(params={"expr": "-3+3"}, expected=0),  # 2
    Dict(params={"expr": "5+0"}, expected=5),  # 3
    Dict(params={"expr": "3.14+5"}, expected=8.14)  # 4
], ids=lambda x: x.expr)
@allure.title("addition test")
@allure.tag("REST API")
def test_addition(scenario):
    r = requests.get("http://api.mathjs.org/v4/", scenario.params)
    assert_that(r.json(), equal_to(scenario.expected), 'Value is match to expected one')


@pytest.mark.parametrize('scenario', [
    Dict(params={"expr": "10-4"}, expected=6),  # 1
    Dict(params={"expr": "-5+-6"}, expected=-11),  # 2
    Dict(params={"expr": "0-3"}, expected=-3),  # 3
    Dict(params={"expr": "7-0.5"}, expected=6.5)  # 4
], ids=lambda x: x.expr)
@allure.title("subtraction test")
@allure.tag("REST API")
def test_subtraction(scenario):
    r = requests.get("http://api.mathjs.org/v4/", scenario.params)
    assert_that(r.json(), equal_to(scenario.expected), 'Value is match to expected one')


@pytest.mark.parametrize('scenario', [
    Dict(params={"expr": "3*5"}, expected=15),  # 1
    Dict(params={"expr": "1*3"}, expected=3),  # 2
    Dict(params={"expr": "10*0"}, expected=0),  # 3
    Dict(params={"expr": "2.5*4"}, expected=10)  # 4
], ids=lambda x: x.expr)
@allure.title("multiplication test")
@allure.tag("REST API")
def test_multiplication(scenario):
    r = requests.get("http://api.mathjs.org/v4/", scenario.params)
    assert_that(r.json(), equal_to(scenario.expected), 'Value is match to expected one')


@pytest.mark.parametrize('scenario', [
    Dict(params={"expr": "8/2"}, expected=4),  # 1
    Dict(params={"expr": "8/6"}, expected=1.3),  # 2
    Dict(params={"expr": "10*0"}, expected=0),  # 3
    Dict(params={"expr": "2.5*4"}, expected=10)  # 4
], ids=lambda x: x.expr)
@allure.title("division test")
@allure.tag("REST API")
def test_division(scenario):
    r = requests.get("http://api.mathjs.org/v4/", scenario.params)
    # check with ilya
    assert_that(r.json(), close_to(scenario.expected-0.1,scenario.expected+0.1), 'Value is close to expected one')


@pytest.mark.parametrize('scenario', [
    Dict(params={"expr": "sqrt(16)"}, expected=4),  # 1
    Dict(params={"expr": "sqrt(sqrt(16))"}, expected=2),  # 2
    # Dict(params={"expr": "sqrt(-4)"}, expected=float("2i")),  # 3
    Dict(params={"expr": "sqrt(4)+sqrt(25)"}, expected=7),  # 4
], ids=lambda x: x.expr)
@allure.title("square root test")
@allure.tag("REST API")
def test_square_root(scenario):
    r = requests.get("http://api.mathjs.org/v4/", scenario.params)
    assert_that(r.json(), equal_to(scenario.expected), 'Value is match to expected one')
