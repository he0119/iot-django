from .settings import *

# Override settings if in production server.
if os.getenv('PRODUCTION_SERVER') == 'true':
    from .production import *

# Override settings if in production server.
if os.getenv('TEST_SERVER') == 'true':
    from .test import *
