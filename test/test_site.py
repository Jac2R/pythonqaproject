from pages.form_fields_page import FormFieldsPage


def test(driver):
    form_fields_page = FormFieldsPage(driver)
    form_fields_page.name_field('Tester')
    form_fields_page.password_field('1111')
    form_fields_page.favorite_drink("water")
    form_fields_page.favorite_drink("coffee")
    form_fields_page.favorite_color("yellow")
    form_fields_page.select_automation('Yes'.lower())
    form_fields_page.email_field('name@example.com')
    form_fields_page.automation_tools()
    form_fields_page.submit_button()

