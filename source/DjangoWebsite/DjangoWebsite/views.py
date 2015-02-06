from django.http import HttpResponse
from django.shortcuts import render_to_response
# import MySQLdb
import datetime
def home(request):
    return render_to_response('home.html')
def current_datetime(request):
    horaServidor = datetime.datetime.now()
    return render_to_response("hora.html", locals())
def nosotros(request):
    titulo = "Nosotros"
    contenido = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    return render_to_response("nosotros.html", locals())
def generar_lista(request, numeroLista):
    titulo = "Listas generadas dinamicamente"
    lista = list()
    for valor in range(int(numeroLista)):
        lista.append("hola mundo esto es el item %s " % valor)
    return render_to_response("lista_generada.html", locals())
def mostrar_datos(request, codigo, nombre, apellido):
    titulo = "%s, %s" % (nombre, apellido)
    return render_to_response("mostrar_datos.html", locals())
def prototype(request):
    return render_to_response("prototype.html")
# def user_list(request):
#     db = MySQLdb.connect(user="chasailx_django", db="chasailx_django_website", pass="djang0", host="http://sail3.com:3306")
#     cursor = db.cursor()
#     cursor.execute('SELECT * FROM books')
#     names = [row[0] for row in cursor.fetchall()]
#     db.close()
#     return render_to_response('book_list.html', {'names': names})
