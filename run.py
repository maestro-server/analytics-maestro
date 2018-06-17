import os
from app import app
from app import views
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# ----------------------------------------
# launch
# ----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("MAESTRO_PORT", 5010))
    app.run(port=port)
