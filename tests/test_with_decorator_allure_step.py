import allure
from selene import browser, by, be


@allure.step("open main page GitHub")
def open_main_page():
    browser.open('/')


@allure.step("search repository")
def search_repository():
    browser.element("//button[@type='button'][@placeholder='Search or jump to...']").click()
    browser.element('#query-builder-test').type('aleksei-pakira/homeWork_10_QA_guru').press_enter()


@allure.step("open found repository")
def open_found_repository():
    browser.element(by.link_text('aleksei-pakira/homeWork_10_QA_guru')).click()


@allure.step("open issues-tab")
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step("check if there is an issue with title 'homework'")
def title_homework_should_exist():
    browser.element(by.partial_text('homework')).should(be.visible)
