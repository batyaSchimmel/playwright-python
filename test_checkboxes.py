from faker import Faker
from playwright.sync_api import Page, expect


fake=Faker()

def test_checkboxes(page: Page) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    page.get_by_label("One").check()
    page.get_by_label("Two").check()
    page.get_by_label("Three").check()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("one, two, three")).to_be_visible()
    page.get_by_text("Selected checkboxes:").click()

