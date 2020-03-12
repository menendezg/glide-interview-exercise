from flask import (Flask, jsonify, abort)
from utils import json_reader

app = Flask(__name__)

offices = json_reader(file='offices.json')
departments = json_reader(file='departments.json')


@app.route("/offices", methods=['GET'])
def get_offices():
    return jsonify({'offices': offices})


@app.route('/offices/<int:office_id>', methods=['GET'])
def get_office_by_id(office_id):
    office = [office for office in offices if office['id'] == office_id]
    if len(office) == 0:
        abort(404)
    return jsonify({'office': office[0]})


@app.route("/departaments")
def get_departments():
    return jsonify({'departments': departments})


@app.route("/departaments/<int:department_id>", methods=['GET'])
def get_departments(departament_id):
    department = [department for department in departments if
                  departments['id'] == departament_id]
    if len(department) == 0:
        abort(404)
    return jsonify({'departament': department[0]})


#---------------------------------------------------------------------------------------
# TODO: Remember, employees I have to get from the url given.
# TODO: i must put a limit default, and api can have the way to
# TODO: pass the limit by query param. ( READ AGAIN )
# @app.route("/employees")
# def hello_world():
#     return jsonify({'offices': offices})

# TODO: make the endpoint for the details of the offices
# --------------------------------------------------------------------------------------