from flask import Flask, json, jsonify, request,Response
from flask_cors import CORS,cross_origin
import sqlite3
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/save_task', methods= ['POST']) 
def post_data():
    json_command=request.json
    json_command = json.dumps(json_command)
    json_command  = json.loads(json_command)
    data=(json_command["data"],json_command["completado"])
    query = ''' INSERT INTO task(name_task,completado)
              VALUES(?,?) '''
    cur.execute(query, data)
    conn.commit()

    return json_command

@app.route('/api/update_task', methods= ['POST']) 
def update_data():
    json_command=request.json
    json_command = json.dumps(json_command)
    json_command  = json.loads(json_command)
    print(json_command)
    query = ''' Update task set name_task = ? where id = ?'''
    data=(json_command["data"],json_command["id"])
    cur.execute(query, data)
    conn.commit()

    return json_command

@app.route('/api/update_complete', methods= ['POST']) 
def update_complete():
    json_command=request.json
    json_command = json.dumps(json_command)
    json_command  = json.loads(json_command)
    print(json_command)
    query = ''' Update task set completado = ? where id = ?'''
    data=(json_command["completado"],json_command["id"],)
    print(data)
    cur.execute(query, data)
    conn.commit()

    return json_command

@app.route('/api/delete_task', methods= ['POST']) 
def delate_data():
    json_command=request.json
    json_command = json.dumps(json_command)
    json_command  = json.loads(json_command)
    print(json_command)
    query = ''' DELETE FROM task WHERE id=?'''
    data=(json_command["id"],)
    cur.execute(query, data)
    conn.commit()

    return json_command


@app.route('/api/get_tasks/', methods= ['GET']) 
def get_data():
    query = ''' INSERT INTO task(name_task)
              VALUES(?) '''
    cur.execute("SELECT * FROM task")
    rows = cur.fetchall()
    json_data=[]
    
    for row in rows:
        json_obj={}
        json_obj["id"]=row[0]
        json_obj["data"]=row[1]
        json_obj["completado"]=row[2]
        json_data.append(json_obj)


    return json_data


if __name__ == "__main__":
    json_command={}
    conn = sqlite3.connect("./to_do_list_db.db",check_same_thread=False)
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE task(id INTEGER PRIMARY KEY, name_task varchar(50) NOT NULL)")
    except:
        print("La tabla ya existe")  


    app.run(host="localhost",port=5001)