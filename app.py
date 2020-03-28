from flask import Flask

from .config import DevelopmentConfig

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object(DevelopmentConfig)


import glide_api.office_resource.views  # F401 isort:skip
import glide_api.department_resource.views  # F401 isort:skip
import glide_api.employee_resource.views  # F401 isort:skip
