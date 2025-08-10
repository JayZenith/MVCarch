from .container import Container
from .views import create_app

def create_application():
    container = Container()
    app = create_app(container)
    return app