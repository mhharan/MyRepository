import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

f = open("C:/Users/3019/machinelearning/pranav/whatsapp/sms.txt", "r")

messages = []
for x in f:
  messages.append(x)
#messages = ["Automated message-Testing 1","Automated message-Testing 2"] #list of messages
print(messages)
f.close()
options = Options()
options.add_argument("--user-data-dir=C:/Users/3019/AppData/Local/Google/Chrome/User Data") #location of chrome user data to open usual chrome window instead of a new window
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


driver = webdriver.Chrome(r'C:\Users\3019\machinelearning\pranav\whatsapp\chromedriver.exe', options=options) #location of selenium chrome driver
driver.maximize_window()
driver.get('https://web.whatsapp.com')

while True:
    try:
        driver.find_element_by_class_name("_27KDP")
        break
    except:
        continue
target = '"ISGEC DevOps Team"' #contact name
panel = driver.find_element_by_id('pane-side')
elem=None
a = 0
while elem is None:
  a += 5
  try:
      driver.execute_script('arguments[0].scrollTop = %s' %a, panel)
      elem = driver.find_element_by_xpath('//span[@title=' + target + ']')

  except:
       continue

ac = ActionChains(driver)
ac.move_to_element(elem).click().perform()
while True:
    for message in messages:
        print(message)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
#        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
        time.sleep(1)

driver.close() #comment out to keep the browser open after program completion