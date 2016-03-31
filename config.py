import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ----------------------------------------------------------------------------
# Base Server Setup
# ----------------------------------------------------------------------------

# Turns on/off application debug mode.
DEBUG = os.environ.get('TORNADO_DEBUG', 'True') == 'True'

# Turns on/off application local mode.
LOCAL = os.environ.get('LOCAL', 'True') == 'True'

# Port at which the app would be listening.
PORT = os.environ.get('PORT', 8000)
