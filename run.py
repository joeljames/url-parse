from app import app
from app.settings import settings

app.run(
    host='0.0.0.0',
    port=settings['PORT'],
    debug=settings['DEBUG']
)
