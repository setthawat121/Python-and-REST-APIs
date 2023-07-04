import sqlite3
from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods =['POST','GET','PUT','DELETE'])
def movie():
    conn = sqlite3.connect('APITest.sqlite')
    c = conn.cursor()
    if request.method == 'POST':
        body = request.get_json()
        c.execute('INSERT INTO movie VALUES (?,?,?,?)', (body['name'], body['years'], body['type'], body['ID']))
        conn.commit()
        return {'successful': body}
    elif request.method == 'GET':
            source = []
            for row in c.execute('SELECT * FROM movie'):
                source.append({"ID": row[3],"name": row[0],"years": row[1],"type": row[2]})
            return {"Get successful" : source}
    elif request.method == 'PUT':
        body = request.get_json()
        c.execute('UPDATE movie SET name = ?, years = ?, type = ? WHERE ID = ?', (body['name'], body['years'], body['type'], body['ID']))
        conn.commit()
        return {'successful': body}
    elif request.method == 'DELETE':
        deleteId = request.args.get('id')
        print(deleteId)
        c.execute('DELETE FROM movie WHERE ID=?', [deleteId])
        conn.commit()
        return {'Message': 'Successful'}

if __name__ == '__main__':
    app.run(debug=True)