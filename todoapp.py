from flask import Flask, render_template #Imoprtamos la libreria Flask

app = Flask(__name__) #Inicializamos la variable.

@app.route('/') #Será responsable de mostrar la lista actual de tareas pendientes en una tabla HTML.
def index():    # y mostrar un formulario HTML para enviar un nuevo elemento de la lista de tareas pendientes.
   return render_template('base.html')

if __name__ == '__main__': #Main del programa.
    app.run(debug=True)