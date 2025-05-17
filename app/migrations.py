import os
from alembic.config import Config
from alembic import command
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def run_alembic_upgrade():
    # Path to alembic.ini file
    alembic_cfg = Config("alembic.ini")

    # Explicitly set the database URL from .env (optional override)
    alembic_cfg.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

    # Run upgrade
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    run_alembic_upgrade()
