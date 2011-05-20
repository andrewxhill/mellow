import os
from paste.deploy import loadapp
here = os.path.dirname(os.path.abspath(__file__))
application = loadapp('config:' + here + '/production.ini')
