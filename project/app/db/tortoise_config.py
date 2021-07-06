import os

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.environ.get("POSTGRES_SERVER"),
                "port": os.environ.get("POSTGRES_PORT"),
                "user": os.environ.get("POSTGRES_USER"),
                "password": os.environ.get("POSTGRES_PASSWORD"),
                "database": os.environ.get("POSTGRES_DB"),
            },
        },
    },
    "apps": {
        "models": {
            "models": [
                "app.models.genres",
                "app.models.movies",
                "aerich.models",
            ],
            "default_connection": "default",
        },
    },
}
