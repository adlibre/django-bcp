# Settings for barcode printer

import os

# Barcode
BAR_HEIGHT = 30
BAR_WIDTH = 0.75 # default is 0.54
BAR_QUIET = False # include l/r whitespace padding.
BAR_CHECKSUM = True

# Label Config
FONT_SIZE = 10
FONT_NAME = 'OCRA'
FONT_PATH = os.path.join(os.path.split(__file__)[0], 'fonts', 'OCRA.ttf',)

# NB It's a better idea to put your settings in a local_settings.py overrides file.
try:
    from local_settings import *
except ImportError:
    pass