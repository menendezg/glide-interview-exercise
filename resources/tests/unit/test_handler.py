from glide_api.resources.businessresource import BusinessResource
from glide_api.resources.tests.unit.expectations.expected_content import (
    expected_employees, expected_expanded_superdepartment)

superdepartments = [
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


def test_handler():
    handler = BusinessResource()
    employees = [
        {
            "first": "Patricia",
            "last": "Diaz",
            "id": 1,
            "manager": None,
            "department": 5,
            "office": 2
        },
        {
            "first": "Daniel",
            "last": "Smith",
            "id": 2,
            "manager": 1,
            "department": 5,
            "office": 2
        },
        {
            "first": "Thomas",
            "last": "Parker",
            "id": 3,
            "manager": None,
            "department": 4,
            "office": None
        }
    ]
    key_words = [['department', 'superdepartment']]
    for keys in key_words:
        employees = [
            handler.handle_lists_key(employee, keys) for employee in employees
        ]
    expected_content = expected_employees

    print(employees)
    assert employees == expected_content


def test_get_item():

    expected_content = {
        "id": 9,
        "name": "Sales Development",
        "superdepartment": 6
    }
    handler = BusinessResource()
    item = handler.get_item(9, superdepartments)
    assert item == expected_content


def test_get_relationship():
    expected_content = expected_expanded_superdepartment
    handler = BusinessResource()
    item = handler.get_relationship({
        "id": 9,
        "name": "Sales Development",
        "superdepartment": 6
    }, 'superdepartment', superdepartments)
    assert item == expected_content
