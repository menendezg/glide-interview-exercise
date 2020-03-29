from glide_api.resources.businessresource import BusinessResource


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
    expected_content = [
        {
            'first': 'Patricia',
            'last': 'Diaz',
            'id': 1,
            'manager': None,
            'department':
            {'id': 5,
             'name': 'Inbound Sales',
             'superdepartment': {
                    'id': 1,
                    'name': 'Sales',
                    'superdepartment': None}
             },
            'office': 2
        },
        {
            'first': 'Daniel',
            'last': 'Smith',
            'id': 2,
            'manager': 1,
            'department': {
                    'id': 5,
                    'name': 'Inbound Sales',
                    'superdepartment':
                        {
                            'id': 1,
                            'name': 'Sales',
                            'superdepartment': None}
            },
            'office': 2},
        {
                'first': 'Thomas',
                'last': 'Parker',
                'id': 3,
                'manager': None,
                'department': {
                    'id': 4,
                    'name': 'Design',
                    'superdepartment': {
                        'id': 3,
                        'name': 'Product',
                        'superdepartment': None}
                },
            'office': None
        }

    ]

    print(employees)
    assert employees == expected_content
