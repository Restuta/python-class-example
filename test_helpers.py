from selenium import webdriver

#abstracts selenium
class KeenMobile:
    def login(self):
        #driver = deriver.Chrome()
       print('login')
    def open_menu(self):
        print('opened menu')
    def logout(self):
        print('logged out')
    def register(self, user_name, password):
        print('registered with user name: ' + user_name + ' and password: ' + password)
