from flask import Flask

app = Flask(__name__)


# ---------------------------------------------------------------------------------------
# TODO: Remember, employees I have to get from the url given.
# TODO: i must put a limit default, and api can have the way to
# TODO: pass the limit by query param. ( READ AGAIN )
# @app.route("/employees")
# def hello_world():
#     return jsonify({'offices': offices})

# TODO: make the endpoint for the details of the offices
# --------------------------------------------------------------------------------------
import glide_api.office_resource.views #F401 isort:skip
import glide_api.department_resource.views #F401 isort:skip
# import glide_api.employee_resource.views #F401 isort:skip
