from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('menu.html')
# ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None  # Variable para almacenar los resultados
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_unitario = 9000
        total_sin_descuento = precio_unitario * cantidad

        # Calcular descuento
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        # Calcular los valores
        monto_descuento = round(total_sin_descuento * descuento)  # Redondea el descuento
        total_con_descuento = round(total_sin_descuento - monto_descuento)  # Redondea el total

        # mensaje del resultado
        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "monto_descuento": monto_descuento,
            "total_con_descuento": total_con_descuento
        }

    return render_template('ejercicio1.html', resultado=resultado)

# ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None  # Variable para almacenar el mensaje
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario in usuarios and usuarios[usuario] == contraseña:
            if usuario == 'juan':
                mensaje = "Bienvenido administrador juan"
            else:
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)