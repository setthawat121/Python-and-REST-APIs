# Python-and-REST-APIs
## API-Python
- ติดตั้ง library และ framework ที่ต้องใช้งาน :
```
!pip install flask
!pip install sqlite3
```
```flask``` คือ framework ที่ใช้สร้าง web application สำหรับ web APIs
<br />```sqlite3``` คือ library ที่ใช้สำหรับการเชื่อมต่อกับ SQlite เพิ่อจัดการข้อมูล
<br />
<br />
- เรียกใช้งานโมดูล ```sqlite3```, ```Flask``` and ```request``` เพื่อนำมารอสำหรับการใช้งานในขั้นตอนถัดไป :
```
import sqlite3
from flask import Flask,request
```
<br />

- เขียนโค้ดสำหรับสร้าง web application โดยเขียนให้อยู่ในรูปแบบพื้นฐาน :
```
app = Flask(__name__)

@app.route('/', methods =['POST','GET','PUT','DELETE'])
def movie():
    return {'Message': 'Successful'}

if __name__ == '__main__':
    app.run(debug=True)
```
โดยเริ่มจากกำหนด ชื่อไฟล์ ```__name__``` โดยการสร้าง Flask ​object แล้วเก็บไว้ใน ```app```
<br />ขั้นตอนต่อมาคือ ```@app.route("/")``` เป็นชื่อ url ของ web browser เพื่อระบุที่อยู่ url ที่ต้องการเรียกใข้งาน 
<br />และต้องระบุ methods ที่ต้องการใข้งานในฟังก์ชั่นด้วย
<br />สุดท้ายเป็นการเรียกดำเนินการรัน web application โดย ```app.run(debug=True)``` 
<br />โดยให้เงื่อนไขเป็นชื่อไฟล์เท่ากับไฟล์หลักที่ใช้รันโปรแกรม
<br />
<br />

- เขียนโค้ดสร้างฟังก์ชั่นสำหรับ request สิ่งที่ต้องการควบคุมฐานข้อมูล :
```
app = Flask(__name__)

@app.route('/', methods =['POST','GET','PUT','DELETE']) 
#กำหนด methods APIs ที่ต้องการใช้งานในฟังก์ชั่น
#POST-เพิ่มข้อมูล, GET-เรียกดูข้อมูล, PUT-แก้ไขข้อมูล, DELETE-ลบข้อมูล
def movie():
    conn = sqlite3.connect('APITest.sqlite') #เชื่อมต่อฐานข้อมูลแล้วเก็บไว้ในตัวแปร conn
    c = conn.cursor() #ระบุ corsor สำหรับชี้ลิ้งที่ต้องการควบคุม
    if request.method == 'POST':
        body = request.get_json()
        c.execute('INSERT INTO movie VALUES (?,?,?,?)', (body['name'], body['years'], body['type'], body['ID']))
        conn.commit()
        return {'successful': body}
        #request method post เป็นเงื่อนไขเพื่อเพิ่มข้อมูลในฐานข้อมูล โดยจะรับข้อมูลในรูปแบบ json 
    elif request.method == 'GET':
        source = []
        for row in c.execute('SELECT * FROM movie'):
        source.append({"ID": row[3],"name": row[0],"years": row[1],"type": row[2]})
        return {"Get successful" : source}
        #request method Get เป็นส่วนที่ใช้ในการเรียกดูข้อมูลที่ต้องการโดยใช้ sql ในการ select ข้อมูลที่ต้องการออกมา
    elif request.method == 'PUT':
        body = request.get_json()
        c.execute('UPDATE movie SET name = ?, years = ?, type = ? WHERE ID = ?', (body['name'], body['years'], body['type'], body['ID']))
        conn.commit()
        return {'successful': body}
        #request method Put สำหรับแก้ไขข้อมูลโดยรับค่าเป็น json
    elif request.method == 'DELETE':
        deleteId = request.args.get('id')
        print(deleteId)
        c.execute('DELETE FROM movie WHERE ID=?', [deleteId])
        conn.commit()
        return {'Message': 'Successful'}
        #request method Delete สำหรับลบข้อมูลในฐานข้อมูล โดยรับค่าเป็น Query id

if __name__ == '__main__':
    app.run(debug=True)
```
<br />

ขั้นตอนต่อไปก็เป็นหน้าที่ของฝ่าย User ที่จะทำการ request ความต้องการผ่าน PostMan
