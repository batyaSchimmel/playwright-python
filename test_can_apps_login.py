from faker import Faker
from playwright.sync_api import Page, expect


fake=Faker()

def test_example(page:Page):
    page.goto('https://canvusapps.com/login')
    page.locator('#email').fill(fake.email())
    page.locator('[name="password"]').fill(fake.password(length=8,digits=True))
    page.get_by_role('checkbox',name='Remember me').check()
    page.get_by_role()
    expect(page).to_have_url('https://canvusapps.com/sessions')
    # expect(page.locator('.alert-block')).to_have_text('')

