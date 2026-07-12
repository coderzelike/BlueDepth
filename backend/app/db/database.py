from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://postgres:Jelszo99@localhost:5432/bluedepth"

engine = create_engine(DATABASE_URL)

print("✅ Connected to BlueDepth database!")