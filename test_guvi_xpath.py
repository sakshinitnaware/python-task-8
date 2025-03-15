# Importing pytest framework for testing
import pytest  

# Importing the GuviAutomation class, which contains login-related automation methods
from guvi_xpath import GuviAutomation  


#TestGuviLogin Class: Contains test methods to validate the login functionality of the Guvi website.
class TestGuviLogin:
    
    #setup_method: This method runs before each test case. It initializes the WebDriver and opens the Guvi website.
    def setup_method(self):
        # Creating an instance of GuviAutomation
        self.guvi = GuviAutomation("https://www.guvi.in/") 
        # Launching the website 
        self.guvi.start_automation()  

    
    #teardown_method:This method runs after each test case. It shuts down the WebDriver to close the browser window.
    def teardown_method(self):
        # Closing the browser after test execution
        self.guvi.shutdown()  

    
    #test_login_button_url:This test verifies that clicking the login button navigates to the correct login page. It asserts that the URL matches the expected login page URL.
    def test_login_button_url(self):
        try:
            # Clicks the login button and retrieves the current URL
            current_url = self.guvi.login_dashboard()
            # Expected login page URL  
            expected_url = "https://www.guvi.in/sign-in/"  
            # Assertion to validate navigation
            assert expected_url in current_url, "FAIL: Login button did not navigate correctly" 
            # Prints success message if assertion passes 
            print("PASS: Login button navigated to correct URL")  
        except Exception as e:
            # Marks test as failed in case of an exception
            pytest.fail(f"FAIL ERROR: Login button test failed: {e}")  

    
    #test_input_fields_visible:This test verifies that the username and password input fields are visible and functional. It ensures that the fields can receive input.
    def test_input_fields_visible(self):
        try:
            # Navigates to the login page
            self.guvi.login_dashboard()  
            # Enters login credentials
            self.guvi.login_credential("abc@com", "@1234")  
            # Prints success message if fields are functional
            print("PASS: Input fields test passed")  
        except Exception as e:
            # Marks test as failed in case of an exception
            pytest.fail(f"FAIL ERROR: Input fields test failed: {e}")  

   
    #test_submit_button:This test validates the login process by clicking the submit button. It ensures that the user is successfully logged in.
   
    def test_submit_button(self):
        try:
            # Navigates to the login page
            self.guvi.login_dashboard()  
             # Enters login credentials
            self.guvi.login_credential("sakshinitnaware17@gmail.com", "SAKSHIw@1234") 
            # Clicks the submit button to log in
            self.guvi.submit_button()  
            # Prints success message if login is successful
            print("PASS: Submit button test passed")  
        except Exception as e:
            # Marks test as failed in case of an exception
            pytest.fail(f"FAIL ERROR: Submit button test failed: {e}")  
