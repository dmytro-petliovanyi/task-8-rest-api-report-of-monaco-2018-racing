from my_app.app import app
from my_app.config import DefaultConfig

if __name__ == "__main__":
    ####################
    # FOR DEVELOPMENT
    ####################
    app.config.from_object(DefaultConfig)
    app.run()
