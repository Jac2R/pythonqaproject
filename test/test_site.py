from pages.form_fields_page import FormFieldsPage


def test_submit_form(driver):
    form_fields_page = FormFieldsPage(driver)
    form_fields_page.name_field('Ivan Ivanov')
    form_fields_page.password_field('Password13')
    form_fields_page.favorite_drink("milk")
    form_fields_page.favorite_drink("coffee")
    form_fields_page.favorite_color("yellow")
    form_fields_page.select_automation('Yes'.lower())
    form_fields_page.email_field('ivan@exmail.com')
    form_fields_page.automation_tools()
    form_fields_page.submit_button()

