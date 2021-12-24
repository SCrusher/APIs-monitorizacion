from flask import Flask, json, jsonify
import subprocess
#from os import system
#import sys
import requests
from requests.api import request
from urllib.request import urlopen, HTTPError, URLError, urlretrieve

app = Flask(__name__)


@app.route('/version')
def verificarVersion():
    ver = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outver = ver.stdout
    return outver

@app.route('/cpu')
def verificarCPU():
    vercpu = subprocess.run(['inxi', '-C'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outcpu = vercpu.stdout
    return outcpu

@app.route('/disk')
def verificarDisk():
    verdisk = subprocess.run(['inxi', '-D'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outdisk = verdisk.stdout
    return outdisk

@app.route('/ram')
def verificarRAM():
    
    free = subprocess.Popen(
    ['free', '-m'],
    stdout=subprocess.PIPE,)

    grep = subprocess.Popen(
    ['grep', 'Mem'],
    stdin=free.stdout,
    stdout=subprocess.PIPE,)

    awk = subprocess.run(
    ['awk', '{print $3/$2*100}'],
    stdin=grep.stdout,
    stdout=subprocess.PIPE,)

    end_pipe = awk.stdout

    return (end_pipe) 

@app.route('/checkstatus/<url>', methods = ["POST"])
def VerificarPagina(url):
    try:
        r = requests.get("http://{}".format(url))
    except requests.exceptions.ConnectionError as e:
        return "Error"
    else:
        if r.status_code == 200:
            return "True"
        else: return r.status_code


    #try:
    #   page_open = urlretrieve("http://{}".format(url))
    #except HTTPError:
    #    return "HTTPError"
    #except URLError:
    #    return "URLError"
    #else:
    #    return "OK"
        
   
   #if r.status_code == 200:
   #     return "true"
   #else: return "false"


#free -m | grep Mem | awk '{print $2}' - MEMORIA RAM TOTAL DEL SISTEMA
#free | grep Mem | awk '{print $3/$2*100}' - PORCENTAJE DE MEMORIA EN USO
#free | grep Mem | awk '{print $4/$2*100}' - PORCENTAJE DE MEMORIA LIBRE


if __name__ == '__main__':
    app.run(debug=True)


