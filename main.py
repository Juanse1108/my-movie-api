from fastapi import FastAPI, Body #importa la clase FastApi de la libreria fastapi
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
        "category": "Action",
    },
    {
        "id": 2,
        "title": "The Matrix",
        "overview": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "year": "1999",
        "rating": 4.1,
        "category": "Action",
    },
    {
        "id": 3,
        "title": "Deadpool",
        "overview": "A wisecracking mercenary gets experimented on and becomes immortal but ugly, and sets out to track down the man who did the dirty work in his eyes.",
        "year": "2016",
        "rating": 4.0,
        "category": "Action",
    },
    {
        "id": 4,
        "title": "Deadpool 2",
        "overview": "Foul-mouthed mutant mercenary Wade Wilson (AKA. Deadpool), brings together a team of fellow survivors to prevent a global catastrophe.",
        "year": "2018",
        "rating": 3.9,
        "category": "Action",
    },
    {
        "id": 5,
        "title": "The Godfather",
        "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "year": "1972",
        "rating": 4.3,
        "category": "Drama",
    },
    {
        "id": 6,
        "title": "The Godfather: Part II",
        "overview": "The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on the family crime syndicate.",
        "year": "1974",
        "rating": 4.3,
        "category": "Drama",
    },
    {
        "id": 7,
        "title": "The Godfather: Part III",
        "overview": "Follows Michael Corleone, now in his 60s, as he seeks to free his family from crime and find a suitable successor to his empire.",
        "year": "1990",
        "rating": 4.3,
        "category": "Drama",
    },
    {
        "id": 8,
        "title": "Intensamente",
        "overview": "When three young men get involved in a crime, the police must prove to them that they are innocent until one of them has an official weapon.",
        "year": "2019",
        "rating": 3.5,
        "category": "Drama",
    },
    {
        "id": 9,
        "title": "The Lord of the Rings: The Return of the King",
        "overview": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
        "year": "2003",
        "rating": 4.5,
        "category": "Fantasy",
    },
    {
        "id": 10,
        "title": "Dragon Ball",
        "overview": "Long ago in the mountains, a fighting master known as Gohan discovered a strange boy whom he named Goku.",
        "year": "1986",
        "rating": 3.5,
        "category": "Fantasy",
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

@app.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str, year: int):
    return [ item for item in movies_list if item["category"] == category ]

@app.post('/movies', tags=['Movies'])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies_list.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies_list

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies_list:
        if item["id"] == id:
            item["title"] = title,
            item["overview"] = overview,
            item["year"] = year,
            item["rating"] = rating,
            item["category"] = category
            return movies_list

@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            movies_list.remove(item)
            return movies_list
    return movies_list