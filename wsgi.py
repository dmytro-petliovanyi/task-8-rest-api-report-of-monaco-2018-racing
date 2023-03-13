from my_app.api import app
from my_app.config import DefaultConfig

if __name__ == "__main__":
    app.config.from_object(DefaultConfig)
    app.run()
