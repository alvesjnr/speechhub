import os


STATIC_PATH = os.path.abspath( __file__ )

EMPTY_INDEX_TEMPLATE = os.path.join(STATIC_PATH,'empty-index.mustache')
INDEX_TEMPLATE = os.path.join(STATIC_PATH,'index.mustache')