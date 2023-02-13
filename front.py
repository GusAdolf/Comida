#IMPORTAR LIBRERIA PARA USAR FRAMEWORK FLASK
from flask import Flask
from flask import render_template
import os
from flask import request
import backend
import numpy as np
##llamado a flask
app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'UPD')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



##servicio web
@app.route('/', methods = ["GET","POST"])
def home():
   
    return render_template('home.html')

#Imagen
@app.route('/success3', methods = ["GET","POST"])  
def success3():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        img = os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
        res = backend.run_example(app.config['UPLOAD_FOLDER'] +'\\'+ f.filename)
        return render_template("home.html", imagen = img, respuesta = res)

@app.route('/info')
def info():
    
    cami = os.path.join(app.config['UPLOAD_FOLDER'], 'cami.jpg')
    gus=os.path.join(app.config['UPLOAD_FOLDER'], 'gus.jpg')
    joss=os.path.join(app.config['UPLOAD_FOLDER'], 'joss.jpg')
    jona=os.path.join(app.config['UPLOAD_FOLDER'], 'jona.jpg')
    alexis=os.path.join(app.config['UPLOAD_FOLDER'], 'alexis.jpeg')
    
    return render_template("info.html", c=cami,g=gus,j=joss,jo=jona,a=alexis)
       
#Frase
@app.route('/submit', methods=["GET","POST"])
def submit():
    
    return render_template('resultados.html')


##ejecutar el servicio web
if __name__=='__main__':
    #OJO QUITAR EL DEBUG EN PRODUCCION
    app.run(host='0.0.0.0', port=5000, debug=True)