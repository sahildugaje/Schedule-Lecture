from flask import Flask,jsonify,request,render_template
import mysql.connector
import datetime

def DBConnection():
        connection = mysql.connector.connect(host='lecture.cechxabyoyas.ap-south-1.rds.amazonaws.com',
	                         database='lecture',
	                         user='lecture',
	                         password='sahild1002')
        #cursor = connection.cursor()
        cursor = connection.cursor()	
        cursor.execute('SELECT * FROM timetable')
        result = cursor.fetchall()
        connection.close()
        return result
        
def getLectureData():
	connection = mysql.connector.connect(host='lecture.cechxabyoyas.ap-south-1.rds.amazonaws.com',
	                         database='lecture',
	                         user='lecture',
	                         password='sahild1002')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM lecture_info')
	lectureData = cursor.fetchall()
	connection.close()
	return lectureData

def getLectureName(courseCode,lectureData):
	for i in lectureData:
		if(lectureData == None):
			return (None)	
		if(courseCode == i[0]):
			return (i[1])        
        
app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome"
	
@app.route('/timetable', methods = ['POST', 'GET'])
def timetable():
	if request.method == 'POST':
		result = request.form
		connection = mysql.connector.connect(host='lecture.cechxabyoyas.ap-south-1.rds.amazonaws.com',
	                         database='lecture',
	                         user='lecture',
	                         password='sahild1002')
		cursor = connection.cursor()
		print(result)
		lectNo = 'lecture'+result['Number']
		print(lectNo)
		if(result['Day'] == 'Monday'):day = 1
		elif(result['Day'] == 'Tuesday'):day = 2
		elif(result['Day'] == 'Wednesday'):day = 3
		elif(result['Day'] == 'Thursday'):day = 4
		elif(result['Day'] == 'Friday'):day = 5
		else:pass
		if(result['Code'] == 'NULL'):cursor.execute("""UPDATE timetable SET """+str(lectNo)+""" = """+(result['Code'])+""" WHERE id ="""+str(day))
		else:cursor.execute("""UPDATE timetable SET """+str(lectNo)+""" = '"""+(result['Code'])+"""' WHERE id ="""+str(day))
		connection.commit()

		
	result = DBConnection()
	lectureData = getLectureData()
	return '''
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
                <script src="extensions/resizable/bootstrap-table-resizable.js"></script>
                <meta name = "viewport" content = "width = device-width, initial-scale = 0.5, shrink-to-fit = no">
		<h2 align = "center" class = "w-auto p-3">Timetable</h2>
		<br>

		<table class="w-auto p-3 h-auto" align="center" border="1" class="table table-bordered">
		  <tr align="center">
		    <th>Day</th>
		    <th>10:00</th>
		    <th>11:00</th>
		    <th>12:45</th>
		    <th>01:45</th>
		    <th>03:00</th>
		  </tr>
		  <tr align="center">
		    <td>'''+ str(result[0][1])+'''</td>
		    <td>'''+ str(getLectureName(str(result[0][2]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[0][3]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[0][4]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[0][5]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[0][6]),lectureData))+'''</td>
		  </tr>
		  <tr align="center">
		    <td>'''+ str(result[1][1])+'''</td>
		    <td>'''+ str(getLectureName(str(result[1][2]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[1][3]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[1][4]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[1][5]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[1][6]),lectureData))+'''</td>
		  </tr>
		  <tr align="center">
		    <td>'''+ str(result[2][1])+'''</td>
		    <td>'''+ str(getLectureName(str(result[2][2]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[2][3]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[2][4]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[2][5]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[2][6]),lectureData))+'''</td>
		  </tr>
		  <tr align="center">
		    <td>'''+ str(result[3][1])+'''</td>
		    <td>'''+ str(getLectureName(str(result[3][2]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[3][3]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[3][4]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[3][5]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[3][6]),lectureData))+'''</td>
		  </tr>
		  <tr align="center">
		    <td>'''+ str(result[4][1])+'''</td>
		    <td>'''+ str(getLectureName(str(result[4][2]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[4][3]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[4][4]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[4][5]),lectureData))+'''</td>
		    <td>'''+ str(getLectureName(str(result[4][6]),lectureData))+'''</td>
		  </tr>
		</table>
		

		<br><br>
		<p align="center" class = "w-auto p-3"><a  href="http://ec2-13-235-31-67.ap-south-1.compute.amazonaws.com:5000/update"><button class="btn btn-secondary">Update Timetable</button></a></p>

		'''
	#return jsonify({'Time Table':result})

@app.route('/timetable/<string:day>', methods = ['GET'])
def timetableDay(day):
	
	if(day == 'Today' or day == 'today'):
		x = datetime.datetime.now()
		day = x.strftime("%A")
	print(day)
	result = DBConnection()
	for i in result:
		if(day == i[1]):
			print(day,i[1])
			return jsonify({'Time Table':i[1:]})
@app.route('/update')
def student():
	return render_template('update.html')

'''@app.route('/update/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		print(result)
		return render_template("result.html",result = result)
'''
if (__name__ == "__main__"):
	app.run(host='0.0.0.0',debug = True)
	
