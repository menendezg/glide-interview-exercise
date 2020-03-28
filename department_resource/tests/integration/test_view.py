

def test_get_all_departments(client):
    departments = [
        {
            "id": 1,
            "name": "Sales",
            "superdepartment": None
        },
        {
            "id": 2,
            "name": "Engineering",
            "superdepartment": None
        },
        {
            "id": 3,
            "name": "Product",
            "superdepartment": None
        },
        {
            "id": 4,
            "name": "Design",
            "superdepartment": 3
        },
        {
            "id": 5,
            "name": "Inbound Sales",
            "superdepartment": 1
        },
        {
            "id": 6,
            "name": "Outbound Sales",
            "superdepartment": 1
        },
        {
            "id": 7,
            "name": "Application Security",
            "superdepartment": 2
        },
        {
            "id": 8,
            "name": "Front-End",
            "superdepartment": 2
        },
        {
            "id": 9,
            "name": "Sales Development",
            "superdepartment": 6
        },
        {
            "id": 10,
            "name": "Product Management",
            "superdepartment": 3
        }
    ]
    url = "/departments"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json == departments


def test_office_by_id(client):
    department = {
        "id": 5,
        "name": "Inbound Sales",
        "superdepartment": 1
    }
    url = "/departments/5"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json == department
