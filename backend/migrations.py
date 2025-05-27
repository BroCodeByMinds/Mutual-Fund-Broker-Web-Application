import os
import subprocess
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
from datetime import datetime

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Define the path to the migrations/versions directory
VERSIONS_DIR = os.path.join(os.path.dirname(__file__), "migrations", "versions")
os.makedirs(VERSIONS_DIR, exist_ok=True)


def create_database_if_not_exists():
    db_url_parts = DATABASE_URL.rsplit('/', 1)
    default_db_url = db_url_parts[0] + '/postgres'
    target_db_name = db_url_parts[1]

    try:
        conn = psycopg2.connect(default_db_url)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{target_db_name}';")
        exists = cur.fetchone()
        if not exists:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(target_db_name)))
            print(f"✅ Database '{target_db_name}' created.")
        else:
            print(f"ℹ️ Database '{target_db_name}' already exists.")
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Failed to create database:", e)


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


def insert_master_family_fund_data():
    """Inserts master data into master.family_fund table."""
    insert_query = """
    INSERT INTO master.family_fund (
        family_fund_id,
        family_fund_name,
        created_date,
        updated_date,
        created_by_user_name,
        updated_by_user_name,
        is_deleted
    ) VALUES %s
    ON CONFLICT (family_fund_id) DO NOTHING;
    """

    values = [
        (1, 'HDFC Mutual Fund', '2025-05-17 21:01:33.375+05:30', '2025-05-17 21:01:33.375+05:30', 'system', 'system', False),
        (2, 'SBI Mutual Fund', '2025-05-17 21:01:33.375+05:30', '2025-05-17 21:01:33.375+05:30', 'system', 'system', False),
        (3, 'ICICI Prudential Mutual Fund', '2025-05-17 21:01:33.375+05:30', '2025-05-17 21:01:33.375+05:30', 'system', 'system', False),
        (4, 'Nippon India Mutual Fund', '2025-05-17 21:01:33.375+05:30', '2025-05-17 21:01:33.375+05:30', 'system', 'system', False),
        (5, 'Axis Mutual Fund', '2025-05-17 21:01:33.375+05:30', '2025-05-17 21:01:33.375+05:30', 'system', 'system', False),
        (6, 'Kotak Mahindra Mutual Fund', '2025-05-17 21:01:33.375+05:30', '2025-05-17 21:01:33.375+05:30', 'system', 'system', False),
        (7, 'Aditya Birla Sun Life Mutual Fund', '2025-05-17 21:01:33.375+05:30', '2025-05-17 21:01:33.375+05:30', 'system', 'system', False),
        (8, 'DSP Mutual Fund', '2025-05-17 21:01:33.375+05:30', '2025-05-17 21:01:33.375+05:30', 'system', 'system', False),
        (9, 'Franklin Templeton Mutual Fund', '2025-05-17 21:01:33.375+05:30', '2025-05-17 21:01:33.375+05:30', 'system', 'system', False),
        (10, 'UTI Mutual Fund', '2025-05-17 21:01:33.375+05:30', '2025-05-17 21:01:33.375+05:30', 'system', 'system', False)
    ]

    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.autocommit = True
        cur = conn.cursor()
        execute_values(cur, insert_query, values)
        print("✅ Master family_fund data inserted.")
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Failed to insert master data:", e)


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
    create_database_if_not_exists()
    create_schema_if_not_exists()
    init_alembic()
    configure_alembic_ini()
    generate_migration()
    upgrade_db()
    insert_master_family_fund_data()
    print("🎉 All done!")

if __name__ == "__main__":
    main()
