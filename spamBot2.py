from selenium import webdriver
#/Users/saabriin/Python\ Bot/chromedriver
driver = webdriver.Chrome('/Users/saabriin/Python Bot/chromedriver')

driver.implicitly_wait(10)
driver.get('https://web.whatsapp.com/')

driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
#inputString = "f u, if you were a dynomite, you wouldnt have enough power to blow your nose. youre a human equivent to a participation award and everyone who ever loved you was wrong!"

while(True):
    with open('random') as file:
      word = file.readline()
      while word:
         driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(" %s" % word.strip())
         driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
         word = file.readline()   

#with open('random') as in_file:
#word = in_file.readline()
#while word:
#word = in_file.readline()

#
#'
