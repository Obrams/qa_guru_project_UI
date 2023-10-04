import os

import allure

from pages.main_page import MainPage


def test_authorization():
    main_page = MainPage()

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization success'):
        main_page.authorization_success()

    with allure.step('Authorization unsuccessful'):
        main_page.authorization_unsuccessful()

    with allure.step('Authorization lock_user'):
        main_page.authorization_lock_user()