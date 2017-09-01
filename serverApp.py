from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
    return Response(

        os.system("echo 'This test will run for quite some time and log wrk2 test data for iteration B adn C'"),

        content_type='text/plain',
    )

config = Configurator()
config.add_route('hello', '/hello')
config.add_view(hello_world, route_name='hello')
app = config.make_wsgi_app()