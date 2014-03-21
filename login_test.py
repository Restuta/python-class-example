from selenium import webdriver
import config
from config import Person
from test_helpers import KeenMobile

person1 = Person(8)
person1.walk()

person2 = Person(159)
person2.walk()

keen_mobile = KeenMobile()
keen_mobile.register('helen', '88888')
keen_mobile.login()
keen_mobile.open_menu()
keen_mobile.logout()

#print ('my person has ' + str(person1.legs) + ' legs')
# driver = webdriver.Chrome()
# driver.get(config.root_url + '#/login')
# driver.quit()

