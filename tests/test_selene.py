from selene import browser, by, be


def test_github_selene():
    browser.open('/')
    browser.element("//button[@type='button'][@placeholder='Search or jump to...']").click()
    browser.element('#query-builder-test').type('aleksei-pakira/homeWork_10_QA_guru').press_enter()
    browser.element(by.link_text('aleksei-pakira/homeWork_10_QA_guru')).click()
    browser.element('#issues-tab').click()

    browser.element(by.partial_text('homework')).should(be.visible)
