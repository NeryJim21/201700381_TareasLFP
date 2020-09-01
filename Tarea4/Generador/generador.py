#Generador de reporte en documento HTML
import webbrowser
#Base de datos
pivote = ''
lista = [
    {
        'nombre': 'Andrés',
        'edad': 18,
        'activo': True,
        'Saldo': 1800
    },
    {
        'nombre': 'Bella',
        'edad': 20,
        'activo': True,
        'Saldo': 800
    },
    {
        'nombre': 'Cesar',
        'edad': 31,
        'activo': True,
        'Saldo': 5800
    },
    {
        'nombre': 'Diana',
        'edad': 19,
        'activo': False,
        'Saldo': 0
    },
    {
        'nombre': 'Estephanie',
        'edad': 22,
        'activo': True,
        'Saldo': 2500
    },
    {
        'nombre': 'Fabio',
        'edad': 26,
        'activo': True,
        'Saldo': 1758
    },
    {
        'nombre': 'Gabriel',
        'edad': 33,
        'activo': False,
        'Saldo': 0
    },
    {
        'nombre': 'Heidi',
        'edad': 24,
        'activo': True,
        'Saldo': 3435
    },
    {
        'nombre': 'Izabel',
        'edad': 45,
        'activo': True,
        'Saldo': 8700
    },
    {
        'nombre': 'Javier',
        'edad': 27,
        'activo': True,
        'Saldo': 30000
    }
]

for n in range(0,len(lista)):
    print()
    print(lista[n]['nombre'])
    print(lista[n]['edad'])
    print(lista[n]['activo'])
    print(lista[n]['Saldo'])
    print()
    print("--------------------")
    
    



#Función para imprimir datos en un archivo HTML
def impresion():

    global pivote
    print("Se tiene que ver chulo :x")

    #Genera HTML
    f = open('reporte.html','w')

    mensaje = """

    <!DOCTYPE html>
    <html>
        <head>
            <title>Reporte</title>
            <link rel=StyleSheet href="stylesheet.css" type="text/css" >
        </head>

        <body>
        <h1><span class="blue"></span>SIMPLE<span class="blue"></span><span class="yellow">QL</pan></h1>
        <h2>REPORTE DE REGISTROS EN BASE DE DATOS</h2>

            <table class="container">
                <thead>
                    <tr>
                        <th><h1>NOMBRE</h1></th>
                        <th><h1>EDAD</h1></th>
                        <th><h1>ACTIVO</h1></th>
                        <th><h1>SALDO</h1></th>
                    </tr>
                </thead>

                <tbody>
     """

    for i in range(0,len(lista)):
        pivote += f""" 
            <tr>
                <td>{lista[i]['nombre']}</td>
                <td>{lista[i]['edad']}</td>
                <td>{lista[i]['activo']}</td>
                <td>{lista[i]['Saldo']}</td>
            </tr>
        """
    
    mensaje2 = """
        </tbody>
                </table>
        </body>
    </html>

    """
    escribir = mensaje+pivote+mensaje2

    f.write(escribir)
    f.close()

    #Genera CSS
    estilo = open('stylesheet.css','w')
    code = """
    /*	
	Side Navigation Menu V2, RWD
	===================
	Author: @heyPablete

    */

    @charset "UTF-8";
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);
    
    body {
    font-family: 'Open Sans', sans-serif;
    font-weight: 300;
    line-height: 1.42em;
    color:#A7A1AE;
    background-color:#1F2739;
    }
    
    h1 {
    font-size:3em; 
    font-weight: 300;
    line-height:1em;
    text-align: center;
    color: #4DC3FA;
    }
    
    h2 {
    font-size:1em; 
    font-weight: 300;
    text-align: center;
    display: block;
    line-height:1em;
    padding-bottom: 2em;
    color: #FB667A;
    }
    
    h2 a {
    font-weight: 700;
    text-transform: uppercase;
    color: #FB667A;
    text-decoration: none;
    }
    
    .blue { color: #185875; }
    .yellow { color: #FFF842; }
    
    .container th h1 {
        font-weight: bold;
        font-size: 1em;
    text-align: left;
    color: #185875;
    }
    
    .container td {
        font-weight: normal;
        font-size: 1em;
    -webkit-box-shadow: 0 2px 2px -2px #0E1119;
            -moz-box-shadow: 0 2px 2px -2px #0E1119;
                box-shadow: 0 2px 2px -2px #0E1119;
    }
    
    .container {
        text-align: left;
        overflow: hidden;
        width: 80%;
        margin: 0 auto;
    display: table;
    padding: 0 0 8em 0;
    }
    
    .container td, .container th {
        padding-bottom: 2%;
        padding-top: 2%;
    padding-left:2%;  
    }
    
    /* Background-color of the odd rows */
    .container tr:nth-child(odd) {
        background-color: #323C50;
    }
    
    /* Background-color of the even rows */
    .container tr:nth-child(even) {
        background-color: #2C3446;
    }
    
    .container th {
        background-color: #1F2739;
    }
    
    .container td:first-child { color: #FB667A; }
    
    .container tr:hover {
        background-color: #464A52;
    -webkit-box-shadow: 0 6px 6px -6px #0E1119;
            -moz-box-shadow: 0 6px 6px -6px #0E1119;
                box-shadow: 0 6px 6px -6px #0E1119;
    }
    
    .container td:hover {
    background-color: #FFF842;
    color: #403E10;
    font-weight: bold;
    
    box-shadow: #7F7C21 -1px 1px, #7F7C21 -2px 2px, #7F7C21 -3px 3px, #7F7C21 -4px 4px, #7F7C21 -5px 5px, #7F7C21 -6px 6px;
    transform: translate3d(6px, -6px, 0);
    
    transition-delay: 0s;
        transition-duration: 0.4s;
        transition-property: all;
    transition-timing-function: line;
    }
    
    @media (max-width: 800px) {
    .container td:nth-child(4),
    .container th:nth-child(4) { display: none; }
    }



    """

    estilo.write(code)
    estilo.close()

    webbrowser.open_new_tab('reporte.html')

impresion()