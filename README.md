# Card Status API

- **GitHub**: https://github.com/Shivkumar-Raghuwanshi/card_api

- **Docker repo**: Docker repo link will added here.

## Overview
The Card Status API provides information about the status of cards. It includes endpoints for getting the status of a card and for getting the status of a card by its ID or user’s contact number.

## Requirements

1. **Python**: The Django framework is written in Python, so you need Python installed on your system to run Django applications. You can download Python from the official website.
2. **Django**: Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. You can install Django by running pip install django in your command line.
3. **Django Rest Framework**: Django Rest Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django. You can install it by running pip install djangorestframework.
4. **Database System:** Django supports several database systems like SQLite, PostgreSQL, MySQL, and Oracle. The default is SQLite and it’s included in the Python standard library.

### Approach

The approach taken in this project is to create a RESTful API using Django and Django Rest Framework. The API includes an endpoint for getting the status of a card by its ID or user’s contact number. The data is stored in a relational database and accessed using Django’s Object-Relational Mapping (ORM) capabilities.

### Choice of Framework/Language

Python was chosen as the programming language due to its readability and ease of use, especially for web development tasks. Python’s extensive standard library and wide range of external libraries make it a versatile language for web development.

**Django was chosen as the web framework for several reasons**:

- It’s written in Python and follows the DRY (Don’t Repeat Yourself) principle, which makes the code easier to maintain and understand.
- It includes a lightweight web server for development, so you can start developing without setting up a separate server.
- It includes an ORM for interacting with the database. This allows you to interact with your data in a Pythonic way instead of writing SQL queries.
- It supports a wide range of databases and includes a database migration system out-of-the-box.
- Django Rest Framework was chosen for creating the API due to its powerful and flexible toolkit for building Web APIs. It includes features like serialization for your models, viewsets for handling the logic of various HTTP methods (GET, POST, etc.), and routers for defining the URLs of your API.

### Possible Improvements

- **Authentication and Permissions**: Currently, the API is open to everyone. Implementing authentication and permissions would ensure that only authorized users can access the data.
- **Pagination**: If the database grows large, returning all entries of a model might become slow Adding pagination to the API would ensure that the server only needs to query a subset of the database for each request.
- **Rate Limiting**: To prevent abuse, you could add rate limiting to the API. This would limit the number of requests a client can make in a certain timeframe.
- Testing: While the API includes some test cases, adding more tests would increase confidence in the correctness of the code. This could include tests for the remaining CRUD operations, tests for the search functionality, and tests for any edge cases you can think of.

### Architectural Decisions

- **Use of SQLite**: SQLite was chosen as the database for this project for its simplicity and because it’s included in the Python standard library. This makes it easy to set up the project without needing to install and configure a separate database server. For a production application, a more robust database system like PostgreSQL or MySQL might be more appropriate.
- **Use of Class-Based Views**: Django Rest Framework’s class-based views were used for handling the API endpoints. This provides a lot of functionality out-of-the-box and allows for better organization and reuse of code.
- **Model Structure**: Each status (Delivered, DeliveryException, Pickup, Returned) and Card is stored in a separate model. This allows each status to have its own fields and makes it easy to add new types of statuses in the future.

## Endpoints
*GET api/get_card_status/*

**Parameters**

- **query**: The card ID or user’s contact number. This parameter is required.

**Response**

The response is a JSON object that contains the status of the card. The status includes Delivered, DeliveryException, Pickup, and Returned objects related to the card. Each object contains the following fields:

- **id**: The ID of the status.

- **card**: The ID of the related card.

- **timestamp**: The timestamp of the status.

- **comment**: The comment of the status. This field is not included in Pickup and Returned objects.

If no card matches the query parameter, the endpoint returns a 404 status code with an error message.

**Example**:
Request:
GET http://localhost:8000/api/get_card_status/?query=test_card

Response:

{
    "Delivered": [
        {
            "id": "test_delivered",
            "card": "test_card",
            "timestamp": "2022-12-31T23:59:59Z",
            "comment": "test_comment"
        }
    ],
    "DeliveryException": [
        {
            "id": "test_delivery_exception",
            "card": "test_card",
            "timestamp": "2022-12-31T23:59:59Z",
            "comment": "test_comment"
        }
    ],
    "Pickup": [
        {
            "id": "test_pickup",
            "card": "test_card",
            "timestamp": "2022-12-31T23:59:59Z"
        }
    ],
    "Returned": [
        {
            "id": "test_returned",
            "card": "test_card",
            "timestamp": "2022-12-31T23:59:59Z"
        }
    ]
}

## Testing
The API includes a test case for the GetCardStatus view. The test case checks the response status code and data when a card is found and when a card is not found. To run the tests, use the py manage.py test for windows and python manage.py test command for Mac.

## Error Handling
The API handles errors gracefully and returns appropriate status codes and error messages. For example, if the query parameter is not provided in the GET /api/get_card_status/ request, the API returns a 400 status code with an error message.