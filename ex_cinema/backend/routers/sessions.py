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

router = APIRouter(prefix="/sessions", tags=["sessions"])

# ЗАДАНИЕ: создай db, next_id, модель SessionIn и 3 эндпоинта
