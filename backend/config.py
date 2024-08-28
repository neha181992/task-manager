import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
