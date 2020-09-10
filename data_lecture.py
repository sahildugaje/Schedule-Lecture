import mysql.connector
import datetime
import time
import scheduleLecture

def DBConnection():
        try:
                connection = mysql.connector.connect(host='lecture.cechxabyoyas.ap-south-1.rds.amazonaws.com',
                                         database='lecture',
                                         user='lecture',
                                         password='sahild1002')
                #cursor = connection.cursor()
                return (connection)
        except Exception as dberror:
                print(dberror)
                scheduleLecture.sendErrorMessage(dberror)
def getLectureName(courseCode):
        try:
                connection = DBConnection()
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM lecture_info WHERE lecture_code = "'+courseCode+'"')
                result = cursor.fetchone()
                courseName = result[1]
                connection.close()
                return(courseName)
        except Exception as e:
                print (e)
                scheduleLecture.sendErrorMessage(e)
        
def getCurrentTimeTable(day):
        try:
                result = get_data(day)
                lec = result[2:]
                m = 1
                courseName = []
                for i in lec:
                        j = getLectureName(i)
                        if(j == None):
                                courseName.append('   '+str(m)+'.  No Lecture')
                        else:
                                courseName.append('  '+str(m)+'. '+j)
                        m = m + 1
                scheduleLecture.scheduleMyself(str(courseName),None)
                scheduleLecture.scheduleIOT(str(courseName),None)
        except Exception as e:
                print(e)
                scheduleLecture.sendErrorMessage(e)
                
def sendData(courseCode):
        try:
                if(courseCode == None):
                        scheduleLecture.scheduleMyself(None,None)
                        scheduleLecture.scheduleIOT(None,None)
                else:
                        get_Meet_Link(courseCode)
        except Exception as e:
                print(e)
                scheduleLecture.sendErrorMessage(e)

def get_Meet_Link(courseCode):
        try:
                connection = DBConnection()
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM lecture_info WHERE lecture_code = "'+courseCode+'"')
                result = cursor.fetchone()
                courseName = result[1]
                meetLink = result[2]
                scheduleLecture.scheduleMyself(courseName,meetLink)
                scheduleLecture.scheduleIOT(courseName,meetLink)
                connection.close()
        except Exception as e:
                print(e)
                scheduleLecture.sendErrorMessage(e) 

def get_data(day):
        try:
                connection = DBConnection()
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM timetable WHERE id = '+str(day))
                result = cursor.fetchone()
                print(result)
                #print(result[lecture_number])
                connection.close()
                return (result)
        except Exception as e:
                print(e)
                scheduleLecture.sendErrorMessage(e)

while(1):
        x = datetime.datetime.now()
        day = x.strftime("%w")
        current_time = x.strftime("%H:%M:%S")	
        
        if(int(day) == 0 or int(day) == 6):
                print("Sleep for 10 hours")
                time.sleep(36000)
        else:
                if(str(current_time) >= '10:00:00' and str(current_time) <= '10:00:30'):
                	getCurrentTimeTable(day)
                	lecture_number = 2
                	result = get_data(day)
                	courseCode = result[lecture_number]
                	sendData(courseCode)
                elif(str(current_time) >= '11:00:00' and str(current_time) <= '11:00:30'):
                        lecture_number = 3
                        result = get_data(day)
                        courseCode = result[lecture_number]
                        sendData(courseCode)
                elif(str(current_time) >= '12:45:00' and str(current_time) <= '12:45:30'):
                        lecture_number = 4
                        result = get_data(day)
                        courseCode = result[lecture_number]
                        sendData(courseCode)
                elif(str(current_time) >= '13:45:00' and str(current_time) <= '13:45:30'):
                        lecture_number = 5
                        result = get_data(day)
                        courseCode = result[lecture_number]
                        sendData(courseCode)
                elif(str(current_time) >= '15:00:00' and str(current_time) <= '15:00:30'):
                        lecture_number = 6
                        result = get_data(day)
                        courseCode = result[lecture_number]
                        sendData(courseCode)
	
        time.sleep(30)
	
		

