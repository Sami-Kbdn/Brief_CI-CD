"""Configuration de la base de données et gestion des sessions.

Ce module gère la connexion à la base de données PostgreSQL
et fournit une fonction générateur pour obtenir des sessions de base de données.
"""

import os
from collections.abc import Generator

from sqlmodel import Session, create_engine

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
port = os.getenv("POSTGRES_PORT")
name = os.getenv("POSTGRES_DB")
host = os.getenv("POSTGRES_HOST")

DATABASE_URL = os.getenv(
    "DATABASE_URL", f"postgresql://{user}:{password}@{host}:{port}/{name}"
)
POOL_SIZE = 10

engine = create_engine(DATABASE_URL)


def get_db() -> Generator[Session]:
    with Session(engine) as session:
        yield session
