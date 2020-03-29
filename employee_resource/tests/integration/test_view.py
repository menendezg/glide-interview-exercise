

def test_get_employees(client):
    employees = [
        {
            "department": {
                "id": 5,
                "name": "Inbound Sales",
                "superdepartment": {
                    "id": 1,
                    "name": "Sales",
                    "superdepartment": None
                }
            },
            "first": "Patricia",
            "id": 1,
            "last": "Diaz",
            "manager": None,
            "office": 2
        },
        {
            "department": {
                "id": 5,
                "name": "Inbound Sales",
                "superdepartment": {
                    "id": 1,
                    "name": "Sales",
                    "superdepartment": None
                }
            },
            "first": "Daniel",
            "id": 2,
            "last": "Smith",
            "manager": {
                "department": 5,
                "first": "Patricia",
                "id": 1,
                "last": "Diaz",
                "manager": None,
                "office": {
                    "address": "20 W 34th St",
                    "city": "New York",
                    "country": "United States",
                    "id": 2
                }
            },
            "office": 2
        },
        {
            "department": {
                "id": 4,
                "name": "Design",
                "superdepartment": {
                    "id": 3,
                    "name": "Product",
                    "superdepartment": None
                }
            },
            "first": "Thomas",
            "id": 3,
            "last": "Parker",
            "manager": None,
            "office": None
        }
    ]
    url = "/employees?limit=3&offset=0&expand=department.superdepartment&expand=manager.office"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json == employees


def test_office_by_id(client):
    employee = {
        "department": 5,
        "first": "Daniel",
        "id": 2,
        "last": "Smith",
        "manager": 1,
        "office": 2
    }
    url = "/employees/2"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json == employee
