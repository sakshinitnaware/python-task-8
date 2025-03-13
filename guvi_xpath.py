

# Import required Selenium modules for browser automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Svc
from webdriver_manager.chrome import ChromeDriverManager as CDM
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#  Run in headless mode
chrome_options.add_argument("--headless")  
#  Disable GPU acceleration (better performance in headless mode)
chrome_options.add_argument("--disable-gpu")  
#  Ensure elements are properly detected
chrome_options.add_argument("--window-size=1920x1080")  
# chrome_options.add_argument("--no-sandbox")  
# #Fix memory-related issues
# chrome_options.add_argument("--disable-dev-shm-usage")  
 
#GuviLocators Class: Stores XPath locators to avoid redundancy and improve maintainability.Helps in keeping test cases clean and easy to update. 
class GuviLocators:
     # XPath for the login button
    LOGIN_BUTTON = '//*[@id="login-btn"]' 
     # XPath for the email input field
    USERNAME_FIELD = '//input[@id="email"]' 
    # XPath for the password input field
    PASSWORD_FIELD = '//input[@id="password"]'  
    # Expected URL after successful login
    DASHBOARD_URL = "https://www.guvi.in/courses/?current_tab=myCourses"  
 
#GuviAutomation Class:Handles automation tasks on the Guvi website. Implements methods for opening the website, logging in, and verifying login success. 
class GuviAutomation:
         
    def __init__(self, url):
        self.url = url  # Store the URL of the website
        self.driver = webdriver.Chrome(service=Svc(CDM().install()), options=chrome_options)  # Initialize Chrome WebDriver
        self.wait = WebDriverWait(self.driver, 10)  # Explicit wait to handle dynamic elements

     
    #start_automation Method: Opens the specified website.Maximizes the browser window.
     
    def start_automation(self):
        try:
            # Open the specified URL
            self.driver.get(self.url)  
             # Maximize browser window
            self.driver.maximize_window() 
            print("Window opened successfully")
        except Exception as E:
            # Handle errors if the page fails to load
            print("Error: Unable to start the automation", E)  
        return True

     
    #login_dashboard Method: Clicks the login button to navigate to the login page.Waits until the login button is clickable before clicking it.  
    def login_dashboard(self):
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, GuviLocators.LOGIN_BUTTON)))  # Wait for the login button
        login_btn.click()  # Click the login button
        print("LOGIN page opened successfully")
        return self.driver.current_url  # Return the current URL after clicking login

     
    #login_credential Method:Takes username and password as input parameters.Waits for the email and password fields to be visible.Inputs the credentials into the respective fields.
     
    def login_credential(self, username, password):
        try:
            # Wait for the email field
            email_field = self.wait.until(EC.presence_of_element_located((By.XPATH, GuviLocators.USERNAME_FIELD)))  
            # Input email
            email_field.send_keys(username)  
            print("PASS: Email entered:", username)
            # Wait for the password field
            password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, GuviLocators.PASSWORD_FIELD)))  
            # Input password
            password_field.send_keys(password)  
            print("PASS: Password entered")
        except Exception as e:
            # Handle exceptions if elements are not found
            print("ERROR: Failed to enter credentials:", e)  

     
    #submit_button Method: Clicks the submit button to log in. Waits until the page is redirected to the dashboard.Validates if the login was successful.
    def submit_button(self):
        try:
            print("Login page URL:", self.driver.current_url)
            # Wait for the submit button
            submit_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, GuviLocators.LOGIN_BUTTON)))  
            submit_btn.click()  # Click the submit button
            # Wait until the dashboard URL is detected
            self.wait.until(EC.url_contains(GuviLocators.DASHBOARD_URL))  
            print("SUCCESS: LOGIN tab clicked")

            # Check if the user has successfully logged in
            if GuviLocators.DASHBOARD_URL in self.driver.current_url:
                print("PASS: Login successful, redirected to dashboard.")
            else:
                # Display if the condition fails
                print("FAIL: Login failed.")
        except Exception as e:
            print("ERROR: Submit button process failed:", e)

     
    #shutdown Method: Closes the browser after execution.Ensures the WebDriver instance is properly quit. 
    def shutdown(self):
        try:
            print("Window closed")
            self.driver.quit()
        except Exception as E:
            print("Error while closing the driver", E)

 
#Main Execution Block: 
# if __name__ == "__main__":
#     guviautomation = GuviAutomation("https://www.guvi.in/")
#     guviautomation.start_automation()
#     guviautomation.login_dashboard()
#     guviautomation.login_credential("test@example.com", "TestPassword123")
#     guviautomation.submit_button()
#     guviautomation.shutdown()
