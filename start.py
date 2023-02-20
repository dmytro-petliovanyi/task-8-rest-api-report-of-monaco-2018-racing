from my_app.config import DefaultConfig
from my_app.views import app

if __name__ == "__main__":
    app.config.from_object(DefaultConfig)
    app.run()
