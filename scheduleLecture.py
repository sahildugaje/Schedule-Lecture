from selenium import webdriver
import time
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\Lecture\scheduleLecture\chromedriver")
driver.get("http://web.whatsapp.com")
time.sleep(45)

def sendErrorMessage(e):
	name = "Myself"
	msg = str(e)
	try:
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()
		time.sleep(1)
		user.click()
                #msg_box = driver.find_element_by_class_name('_3FRCZ')
		msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		msg_box.click()
		time.sleep(1)
		msg_box.send_keys(msg)
		time.sleep(1)
		driver.find_element_by_class_name('_1U1xa').click()
		print("Error Message sent")
		time.sleep(2)
	except Exception as err:
		print(err)


def scheduleMyself(courseName,meetLink):
	name = "Myself"
	if(courseName == None and meetLink == None):
		msg = 'No Lecture'
	elif(meetLink == None):
		msg = str("Today's Lectures are:      "+courseName)
	else:
		msg = str(courseName+':	 '+meetLink)
	try:
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()
		time.sleep(1)
		user.click()
                #msg_box = driver.find_element_by_class_name('_3FRCZ')
		msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		msg_box.click()
		time.sleep(1)
		msg_box.send_keys(msg)
		time.sleep(1)
		driver.find_element_by_class_name('_1U1xa').click()
		print("Message sent to Myself")
		time.sleep(2)
	except Exception as e:
		print("Could not Connect to Whatsapp.com")
		print("Error", e)
		sendErrorMessage(e)
def scheduleIOT(courseName,meetLink):
	name = "IoT Chichore"
	if(courseName == None and meetLink == None):
		msg = 'No Lecture'
	elif(meetLink == None):
		msg = str("Today's Lectures are:      "+courseName)
	else:
		msg = str(courseName+':	 '+meetLink)
	try:
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()
		time.sleep(1)
		user.click()
		#msg_box = driver.find_element_by_class_name('_3FRCZ')
		msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		msg_box.click()
		time.sleep(1)
		msg_box.send_keys(msg)
		time.sleep(1)
		driver.find_element_by_class_name('_1U1xa').click()
		print("Message sent to IOT Group")
		time.sleep(2)
	except Exception as e1:
		print("Could not Connect to Whatsapp.com")
		print("Error", e1)
		sendErrorMessage(e1)
		
