from fastapi import FastAPI #importa la clase FastApi de la libreria fastapi
from fastapi.responses import HTMLResponse #importa la clase HTMLResponse de la libreria fastApi

app = FastAPI() #crea una instancia de la clase FastApi
app.title = "Mi aplicacion con FastAPI" #asigna un valor al atributo title
app.version = "0.0.1"

movies_list = [
    {
        "id": 1,
        "title": "Fast and the Furious",
        "overview": "Dom and Brian are forced to work together when a mysterious,ompromising plot prevents them from meeting their goals.",
        "year": "2001",
        "rating": 4.2,
    },
    {
        "id": 2,
        "title": "The Matrix",
        "overview": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "year": "1999",
        "rating": 4.1,
    }
]
@app.get('/', tags=['Home']) #definimos la ruta
def message(): #definimos la funcion de la ruta
    return HTMLResponse('<h1>Hola mundo</h1>')

@app.get('/movies', tags=['Movies'])
def movies():
    return movies_list

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item
    return []