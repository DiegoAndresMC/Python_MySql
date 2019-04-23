from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
#Configura conexion bd 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

#configuracion
app.secret_key = 'secretkey'

#ruta principal index
@app.route('/')
def index():
	return render_template('index.html')
#ruta cntacto nuevo, que lo en via al formulario html
@app.route('/add_contacto', methods=['POST'])
def add_contacto():
	if request.method == 'POST':
		fullname = request.form['fullname']
		telefono = request.form['telefono']
		email = request.form['email']
		cur = mysql.connection.cursor()		
		cur.execute('INSERT INTO contactos (fullname, telefono, email) VALUES (%s, %s, %s)', 
			(fullname, telefono, email))
		mysql.connection.commit()
		flash('Contacto Agregado Correctamente')
		return redirect(url_for('index'))
@app.route('/edit')
def edit():
	return 'Edit'

@app.route('/eliminar')
def eliminar():
	return 'eliminar'


if __name__ == '__main__':
	app.run(port = 5000, debug=True)