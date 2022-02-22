import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window
        driver.implicitly_wait(5)
        
    def test_new_user(self):
        #Seleccionar la opcion log in
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()
        
        #Crear variable para el boton "Crear cuenta" de la pagina
        create_account_button=driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        #Asegurase de que el boton este disponible y se pueda ver. Si es así, darle click
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()        
        #Asegurarse de que se esta en la pestaña "Crear cuenta" de la pagina
        self.assertEqual("Create New Customer Account", driver.title)

        first_name=driver.find_element_by_id("firstname")
        middle_name=driver.find_element_by_id("middlename")
        last_name=driver.find_element_by_id("lastname")
        email_address=driver.find_element_by_id("email_address")
        news_letter_subscription=driver.find_element_by_id("is_subscribed")
        password=driver.find_element_by_id("password")
        confirm_password=driver.find_element_by_id("confirmation")
        submit_button=driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        first_name.send_keys("Test")
        driver.implicitly_wait(1)
        middle_name.send_keys("Test")
        driver.implicitly_wait(1)
        last_name.send_keys("Test")
        driver.implicitly_wait(1)
        email_address.send_keys("Test@testingmail.com")
        driver.implicitly_wait(1)
        password.send_keys("Test")
        driver.implicitly_wait(1)
        confirm_password.send_keys("Test")
        driver.implicitly_wait(50)
        submit_button.click()
        


    def tearDown(self):
        self.driver.implicitly_wait(10)
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)