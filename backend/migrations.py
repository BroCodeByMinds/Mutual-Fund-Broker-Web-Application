import os
import subprocess
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Define the path to the migrations/versions directory
VERSIONS_DIR = os.path.join(os.path.dirname(__file__), "migrations", "versions")
os.makedirs(VERSIONS_DIR, exist_ok=True)

def create_schema_if_not_exists():
    """Creates the 'master' schema in the PostgreSQL database if it doesn't exist."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("CREATE SCHEMA IF NOT EXISTS master;")
        print("✅ 'master' schema ensured.")
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Failed to create schema:", e)

def init_alembic():
    """Initializes Alembic if not already initialized."""
    if not os.path.exists("alembic"):
        subprocess.run(["alembic", "init", "alembic"])
        print("✅ Alembic initialized.")
    else:
        print("ℹ️ Alembic already initialized.")

def configure_alembic_ini():
    """Configures alembic.ini with the DATABASE_URL."""
    ini_path = "alembic.ini"
    if not os.path.exists(ini_path):
        print("❌ alembic.ini not found.")
        return

    with open(ini_path, "r") as file:
        lines = file.readlines()

    with open(ini_path, "w") as file:
        for line in lines:
            if line.strip().startswith("sqlalchemy.url"):
                file.write(f"sqlalchemy.url = {DATABASE_URL}\n")
            else:
                file.write(line)

    print("✅ alembic.ini configured.")

def generate_migration():
    """Generates the initial Alembic migration script."""
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", "Initial migration"])
    print("✅ Migration script created.")

def upgrade_db():
    """Applies the Alembic migration (upgrade head)."""
    subprocess.run(["alembic", "upgrade", "head"])
    print("✅ Database upgraded.")

def main():
    print("🚀 Starting Alembic setup and migration...")
    create_schema_if_not_exists()
    init_alembic()
    configure_alembic_ini()
    generate_migration()
    upgrade_db()
    print("🎉 All done!")

if __name__ == "__main__":
    main()
