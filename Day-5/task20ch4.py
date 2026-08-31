from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://practicesoftwaretesting.com/"

scenarios = [
    {
        "name": "Empty first name",
        "first_name": "",
        "last_name": "C",
        "email": "vasudevan.c@matodata.com",
        "password": "Vasu31.7.4",
        "address": "Sivagangai",
        "expected_error": "First name is required"
    },
    {
        "name": "Empty last name",
        "first_name": "Vasu",
        "last_name": "",
        "email": "vasudevan.c@matodata.com",
        "password": "Vasu31.7.4",
        "address": "Sivagangai",
        "expected_error": "Last name is required"
    },
    {
        "name": "Invalid email",
        "first_name": "Vasu",
        "last_name": "C",
        "email": "invalid-email",
        "password": "Vasu31.7.4",
        "address": "Sivagangai",
        "expected_error": "Email format is invalid"
    },
    {
        "name": "Missing password",
        "first_name": "Vasu",
        "last_name": "C",
        "email": "vasudevan.c@matodata.com",
        "password": "",
        "address": "Sivagangai",
        "expected_error": "Password is required"
    },
    {
        "name": "Invalid password",
        "first_name": "Vasu",
        "last_name": "C",
        "email": "vasudevan.c@matodata.com",
        "password": "123",
        "address": "Sivagangai",
        "expected_error": "Password must be minimal 6 characters long"
    },
    {
        "name": "Missing address",
        "first_name": "Vasu",
        "last_name": "C",
        "email": "vasudevan.c@matodata.com",
        "password": "Vasu31.7.4",
        "address": "",
        "expected_error": ""
    },
    {
        "name": "Valid registration",
        "first_name": "Vasu",
        "last_name": "C",
        "email": "vasudevan.c@matodata.com",
        "password": "Vasu31.7.4",
        "address": "Sivagangai",
        "expected_error": ""
    }
]

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    for scenario in scenarios:

        print("\nScenario:", scenario["name"])

        page.goto(BASE_URL + "auth/register")
        page.wait_for_load_state("networkidle")

        page.locator("input[data-test='first-name']").fill(scenario["first_name"])
        page.locator("input[data-test='last-name']").fill(scenario["last_name"])
        page.locator("input[data-test='dob']").fill("1995-01-01")
        page.locator("select[data-test='country']").select_option("IN")
        page.locator("input[data-test='postal_code']").fill("600001")
        page.locator("input[data-test='house_number']").fill("10")
        page.locator("input[data-test='street']").fill(scenario["address"])
        page.locator("input[data-test='city']").fill("Sivagangai")
        page.locator("input[data-test='state']").fill("Tamil Nadu")
        page.locator("input[data-test='phone']").fill("9876543210")
        page.locator("input[data-test='email']").fill(scenario["email"])
        page.locator("input[data-test='password']").fill(scenario["password"])
        page.get_by_role("button",name="Register").click()

        page.wait_for_timeout(1000)

        if scenario["name"] == "Valid registration":

            expect(page).not_to_have_url(BASE_URL + "auth/register")

            print("Registration: SUCCESSFUL")
            print("Result: PASS")

        else:

            assert "/auth/register" in page.url

            if scenario["name"] == "Missing address":

                print("Registration: NOT successful")
                print("Address value:", scenario["address"])
                print("Result: PASS")

            else:

                error_message = page.get_by_role("alert")

                expect(error_message).to_contain_text(scenario["expected_error"])
                print("Registration: NOT successful")
                print("Validation message:",error_message.text_content().strip())
                print("Result: PASS")
    
    print("Scenarios tested:", len(scenarios))
    print("All scenarios completed")

    browser.close()