

def test_get_all_offices(client):
    office_list = [
        {
            "address": "450 Market St",
            "city": "San Francisco",
            "country": "United States",
            "id": 1
        },
        {
            "address": "20 W 34th St",
            "city": "New York",
            "country": "United States",
            "id": 2
        },
        {
            "address": "32 London Bridge St",
            "city": "London",
            "country": "United Kingdom",
            "id": 3
        },
        {
            "address": "233 S Wacker Dr",
            "city": "Chicago",
            "country": "United States",
            "id": 4
        },
        {
            "address": "1 Chome-1-2 Oshiage, Sumida City",
            "city": "Tokyo",
            "country": "Japan",
            "id": 5
        }
    ]
    url = "/offices"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json == office_list


def test_office_by_id(client):
    office = {
        "address": "450 Market St",
        "city": "San Francisco",
        "country": "United States",
        "id": 1
    }
    url = "/offices/1"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json == office
