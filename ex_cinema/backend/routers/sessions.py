"""Роутер СЕАНСОВ — ЗАДАНИЕ.

═══════════════════════════════════════════════════════════════
ЗАДАНИЕ: реализуй 3 эндпоинта для управления сеансами

Модель данных сеанса:
{
    "id": 1,
    "movie_id": 1,        # привязка к фильму (должен существовать!)
    "time": "18:00",      # время сеанса
    "price": 450,         # цена билета (> 0)
    "seats": 50           # кол-во мест (> 0)
}

Начальные данные (скопируй в db):
[
    {"id": 1, "movie_id": 1, "time": "18:00", "price": 450, "seats": 50},
    {"id": 2, "movie_id": 1, "time": "21:00", "price": 550, "seats": 30},
    {"id": 3, "movie_id": 2, "time": "19:30", "price": 400, "seats": 60},
]

Что нужно реализовать:

1. GET /sessions/?movie_id=<int>  (необязательный query-параметр)
   - Без параметра → вернуть все сеансы
   - С movie_id → только сеансы этого фильма
   - Подсказка: посмотри как работает Query в FastAPI

2. POST /sessions/  (принимает SessionIn)
   - SessionIn: movie_id (int), time (str), price (int), seats (int)
   - ВАЖНО: проверь что фильм с movie_id существует!
     Для этого импортируй: from routers.movies import db as movies_db
     и поищи фильм в movies_db
   - Если фильм не найден → HTTPException(404, "Фильм не найден")
   - price > 0, seats > 0, time не пустой
   - Верни созданный сеанс, status_code=201

3. DELETE /sessions/{session_id}  (status_code=204)
   - Удалить сеанс по id
   - Если не найден → 404

═══════════════════════════════════════════════════════════════
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from routers import movies

router = APIRouter(prefix="/sessions", tags=["sessions"])

db: list[dict] =
    [
        {"id": 1, "movie_id": 1, "time": "18:00", "price": 450, "seats": 50},
        {"id": 2, "movie_id": 1, "time": "21:00", "price": 550, "seats": 30},
        {"id": 3, "movie_id": 2, "time": "19:30", "price": 400, "seats": 60},
    ]
   next_id = 4
   
 class SessionIn(BaseModel): 
    movie_id: int
    time: str
    price: int
    seats: int
   
@router.get("/")
def get_sessions(movie_id: int | None = Query(None)):
    if movie_id is not None:
        return [s for s in db if s["movie_id"] == movie_id]
    return db   
    
@router.post("/", status_code=201)
def add_session(body: SessionIn):

    # Проверка существования фильма
    movie_exists = any(m["id"] == body.movie_id for m in movies.db)
    if not movie_exists:
        raise HTTPException(404, "Фильм не найден")
    
    # Валидация данных
    if not body.time.strip():
        raise HTTPException(400, "Время сеанса не может быть пустым")
    if body.price <= 0:
        raise HTTPException(400, "Цена должна быть больше 0")
    
    global next_id
    session = {
        "id": next_id,
        "movie_id": body.movie_id,
        "time": body.time.strip(),
        "price": body.price,
        "seats": body.seats,
    }
    db.append(session)
    next_id += 1
    return session
    
    
@router.delete("/{session_id}", status_code=204)
def delete_session(session_id: int):
    global db
    before = len(db)
    db = [s for s in db if s["id"] != session_id]
    if len(db) == before:
        raise HTTPException(404, "Сеанс не найден")

# ЗАДАНИЕ: создай db, next_id, модель SessionIn и 3 эндпоинта
