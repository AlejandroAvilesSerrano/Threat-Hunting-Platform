
from api.factory import create_api_app
from composition.bootstrap import bootstrap

components = bootstrap()
app = create_api_app(components)