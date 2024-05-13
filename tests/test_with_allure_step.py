import allure
from selene import browser, by, be


def test_with_allure_step():
    with allure.step("open main page GitHub"):
        browser.open('/')

    with allure.step("search repository"):
        browser.element("//button[@type='button'][@placeholder='Search or jump to...']").click()
        browser.element('#query-builder-test').type('aleksei-pakira/homeWork_10_QA_guru').press_enter()

    with allure.step("open found repository"):
        browser.element(by.link_text('aleksei-pakira/homeWork_10_QA_guru')).click()

    with allure.step("open issues-tab"):
        browser.element('#issues-tab').click()

    with allure.step("check if there is an issue with title 'homework'"):
        browser.element(by.partial_text('homework')).should(be.visible)
