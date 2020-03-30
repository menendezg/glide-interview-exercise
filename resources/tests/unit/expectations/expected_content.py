expected_employees = [
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

expected_expanded_superdepartment = {
    "id": 9,
    "name": "Sales Development",
    "superdepartment": {
            "id": 6,
            "name": "Outbound Sales",
            "superdepartment": 1
    },
}
