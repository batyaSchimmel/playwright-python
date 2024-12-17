from faker import Faker
from playwright.sync_api import Page, expect


fake=Faker()

def test_example(page:Page):
    page.goto('https://canvusapps.com/signup')
    page.locator('#user_name').fill(fake.user_name())
    page.locator('#user_email').fill(fake.email())
    password=fake.password(length=8,digits=True)
    page.locator('#user_password').fill(password)
    page.locator('#user_password_confirmation').fill(password)
    page.locator('[name="company[name]"]').fill(fake.company())
    # page.get_by_role('checkbox',name='Remember me').check()
    page.get_by_role('button',name='Sign up').click()
    # expect(page).to_have_url('https://canvusapps.com/sessions')
    expect(page.locator('.alert-block')).to_have_text("We couldn't setup your account. Please try a different browser or device.")

