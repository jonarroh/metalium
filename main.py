import models.test
from server.fastapi.init import CreateFastAPIServer
from storage.sqlite.adapter import SQLiteAdapter
import os
import models
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

def main():
    print("Starting server...")
    adapter = SQLiteAdapter(database_url=os.getenv('DATABASE_URL'))

    new_test = models.test.Test(name="Test", description="This is a test")
    adapter.saveOne(new_test)

    result = adapter.execute("SELECT * FROM test")
    print(result)


if __name__ == "__main__":
    main()
