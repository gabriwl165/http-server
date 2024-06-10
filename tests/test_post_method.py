# test_app.py
import json

import requests


def test_post_json():
    # Define your JSON data
    data = {
        "person": {
            "name": "John Doe",
            "age": 30,
            "email": "johndoe@example.com",
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "zipcode": "12345",
                "country": "USA"
            },
            "phones": [
                {
                    "type": "home",
                    "number": "555-1234"
                },
                {
                    "type": "work",
                    "number": "555-5678"
                }
            ],
            "is_active": True,
            "tags": ["developer", "python", "flask"]
        },
        "products": [
            {
                "name": "Product A",
                "price": 10.99,
                "quantity": 100
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            },
            {
                "name": "Product B",
                "price": 20.49,
                "quantity": 50
            },
            {
                "name": "Product C",
                "price": 5.99,
                "quantity": 200
            }
        ]
    }

    # Send a POST request to "/"
    response = requests.post(f"http://localhost:1234/", json=data)
