"""WSGI entry for hosts like Render and PythonAnywhere (they do not run `python run.py`)."""
from thaghrah import create_app
from thaghrah.db import init_db

init_db()
application = create_app()
app = application
