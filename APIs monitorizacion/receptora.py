from flask import Flask, request, redirect, url_for, render_template, json, jsonify
from app import verificarCPU
from conexion import *
import requests
#from requests.api import request

app = Flask(__name__)

@app.route('/app')
def app_page():
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    consulta = "SELECT * FROM applications"
    cur.execute(consulta)
    list_apps = cur.fetchall()
    return render_template('app.html', list_apps=list_apps)

@app.route('/add_app', methods=['POST'])
def add_app():
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        application_name = request.form['application_name']
        application_type = request.form['application_type']
        url = request.form['url']
        cur.execute("INSERT INTO applications(application_name, application_type, url) VALUES (%s, %s, %s)", (application_name, application_type, url))
        conn.commit()
    return redirect(url_for('app_page'))

@app.route('/app/update/<id>', methods=['POST'])
def update_app(id):
    if request.method == 'POST':
        edit_name = request.form['edit_name']
        edit_type = request.form['edit_type']
        edit_url = request.form['edit_url']
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("UPDATE applications SET application_name = %s, application_type = %s, url = %s WHERE id = %s", (edit_name, edit_type, edit_url, id))
        conn.commit()
        return redirect(url_for('app_page'))

@app.route('/app/delete/<id>', methods=['POST'])
def delete_app(id):
    if request.method == 'POST':
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("DELETE FROM applications WHERE id = %s", (id))
        rows_deleted = cur.rowcount
        conn.commit()
        return redirect(url_for('app_page'))


@app.route('/mostrar_logs')
def mostrar_logs():
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    consulta = "SELECT application_name, application_id, created_at, app_log from applications, applications_logs where applications.id = applications_logs.application_id"
    cur.execute(consulta)
    list_log = cur.fetchall()
    return render_template('log.html', list_log=list_log)


#INSERT into applications_logs(application_id, created_at, app_log)values (1, now(),'{}')#

@app.route('/consultar_app/<id>', methods=['GET','POST'])
def consultar_app(id):
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT url from applications where id = %s",(id))
    url = cur.fetchone()
    datos_log = {"Version" : conecta2("version",'GET').decode(),
                 "Cpu": conecta2("cpu",'GET').decode(),
                 "Ram": conecta2("ram",'GET').decode(),
                 "Disk": conecta2("disk",'GET').decode(),
                 "Status": conecta2("checkstatus/{}".format (url[0]),'POST').decode()}
    #json_datalog = json.dumps(datos_log)
    cur.execute("INSERT INTO applications_logs(application_id, app_log) VALUES (%s, %s)", (id, json.dumps(datos_log)))
    conn.commit()
    return ("Log ingresado")

def conecta2(path, method):
    try:
        if method == 'GET':
            r = requests.get("http://localhost:5000/{}".format(path))
        elif method == 'POST':
            r = requests.post("http://localhost:5000/{}".format(path))
    except requests.exceptions.ConnectionError as e:
        return "Error"
    else:
        if r.status_code == 200:
            print(r)
            return r.content
        else: return "False"

if __name__ == '__main__':
    app.run(debug=True, port=4000)

