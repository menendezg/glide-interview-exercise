from flask import Flask

app = Flask(__name__)


import glide_api.office_resource.views  # F401 isort:skip
import glide_api.department_resource.views  # F401 isort:skip
import glide_api.employee_resource.views  # F401 isort:skip
