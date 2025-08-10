from .container import Container
from .views import create_app


# Entry points of application
# create_application() initializes Container
def create_application():
    container = Container()
    app = create_app(container)
    return app