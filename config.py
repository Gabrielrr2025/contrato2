import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///contratos.db")
    TEMPLATES_DIR = "templates"
    OUTPUT_DIR = "contratos_gerados" 
    UPLOADS_DIR = "uploads"

    DEFAULT_ADMIN_USER = "admin"
    DEFAULT_ADMIN_PASS = "admin123"

    DEFAULT_FONT = "Times New Roman"
    DEFAULT_FONT_SIZE = 12
