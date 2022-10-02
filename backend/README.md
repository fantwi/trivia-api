# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Error Handling
Errors are returned as JSON objects in the following format:
```
{
  'success': False,
  'error': 400,
  'message': 'bad request'
}
```
The API will return five error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Unprocessable Entity
- 500: Internal Server Error

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### `GET '/categories'`
- General:
    - Returns a dictionary of all category objects and success value. The keys of the dictionary are the ids and the values are their corresponding string category types.
- Sample: `curl http://127.0.0.1:5000/categories`
- Response:
    ``` {
      "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
      },
      "success": true
    }
    ```

### `GET '/questions?page={page_number}'`
- General: 
    - Returns a dictionary of all question objects, all categories, current category, total number of questions and success value. 
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/questions?page=2`
- Response:
    ```{
      "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
      },
      "current_category": {
        "4": "History"
      },
      "questions": [
        {
          "answer": "One",
          "category": "2",
          "difficulty": 4,
          "id": 18,
          "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
          "answer": "Jackson Pollock",
          "category": "2",
          "difficulty": 2,
          "id": 19,
          "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
          "answer": "The Liver",
          "category": "1",
          "difficulty": 4,
          "id": 20,
          "question": "What is the heaviest organ in the human body?"
        },
        {
          "answer": "Alexander Fleming",
          "category": "1",
          "difficulty": 3,
          "id": 21,
          "question": "Who discovered penicillin?"
        },
        {
          "answer": "Blood",
          "category": "1",
          "difficulty": 4,
          "id": 22,
          "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
          "answer": "Scarab",
          "category": "4",
          "difficulty": 4,
          "id": 23,
          "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        },
        {
          "answer": "Somebody special",
          "category": "5",
          "difficulty": 5,
          "id": 24,
          "question": "Who is your best friend"
        },
        {
          "answer": "Somebody special",
          "category": "1",
          "difficulty": 3,
          "id": 25,
          "question": "Who is your best friend"
        },
        {
          "answer": "Somebody special",
          "category": "5",
          "difficulty": 3,
          "id": 26,
          "question": "Who is your best friend"
        },
        {
          "answer": "atebuby",
          "category": "4",
          "difficulty": 4,
          "id": 27,
          "question": "where are you from "
        }
      ],
      "success": true,
      "total_questions": 23
    ```

### `DELETE '/questions/{book_id}'`
- General:
    - Deletes the question with the given ID if it exists. Returns the id of the deleted question, success value, total questions, and list of questions based on the current page number to update the frontend.
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/22?page=2`
- Response:
    ``` {
      "deleted": 22,
      "questions": [
        {
          "answer": "One",
          "category": "2",
          "difficulty": 4,
          "id": 18,
          "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
          "answer": "Jackson Pollock",
          "category": "2",
          "difficulty": 2,
          "id": 19,
          "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
          "answer": "The Liver",
          "category": "1",
          "difficulty": 4,
          "id": 20,
          "question": "What is the heaviest organ in the human body?"
        },
        {
          "answer": "Alexander Fleming",
          "category": "1",
          "difficulty": 3,
          "id": 21,
          "question": "Who discovered penicillin?"
        },
        {
          "answer": "Scarab",
          "category": "4",
          "difficulty": 4,
          "id": 23,
          "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        },
        {
          "answer": "Somebody special",
          "category": "5",
          "difficulty": 5,
          "id": 24,
          "question": "Who is your best friend"
        },
        {
          "answer": "Somebody special",
          "category": "1",
          "difficulty": 3,
          "id": 25,
          "question": "Who is your best friend"
        },
        {
          "answer": "Somebody special",
          "category": "5",
          "difficulty": 3,
          "id": 26,
          "question": "Who is your best friend"
        },
        {
          "answer": "atebuby",
          "category": "4",
          "difficulty": 4,
          "id": 27,
          "question": "where are you from "
        },
        {
          "answer": "Elknow",
          "category": "3",
          "difficulty": 1,
          "id": 28,
          "question": "What is your department"
        }
      ],
      "success": true,
      "total_questions": 22
    }
    ```

###  `POST '/questions'`
- General:
    - Creates a new question using the submitted question, answer, category, and difficulty. Returns the id of the created question, success value, total questions, and list of questions based on the current page number to update the frontend.
- Sample: `curl http://127.0.0.1:5000/questions?page=3 -X POST -H "Content-Type: application/json" -d '{"question":"Who was the president of Ghana in 2015", "answer":"John Mahama", "category": "4", "difficulty": "3"}'`
- Response:
    ``` {
      "created": 31,
      "questions": [
        {
          "answer": "Jollof rice",
          "category": "4",
          "difficulty": 2,
          "id": 29,
          "question": "What is your favorite food"
        },
        {
          "answer": "Kwame Nkrumah",
          "category": "4",
          "difficulty": 3,
          "id": 30,
          "question": "Who led the fight for Ghana's independence"
        },
        {
          "answer": "John Mahama",
          "category": "4",
          "difficulty": 3,
          "id": 31,
          "question": "Who was the president of Ghana in 2015"
        }
      ],
      "success": true,
      "total_questions": 23
    }
    ```

### `POST '/questions/search'`
- General:
    - Returns a list of questions containing the searchTerm, success value, and total questions. 
- Sample: `curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type": "application/json" -d '{"searchTerm":"clay"}'`
- Response:
    ``` {
      "questions": {
          "answer": "Muhammad Ali",
          "category": "4",
          "difficulty": 1,
          "id": 9,
          "question": "What boxer's original name is Cassius Clay?"
        }
      }
    ```

### `GET '/categories/{category_id}/questions'`
- General:
    - Returns a dictionary of all question objects based on the selected category paginated into groups of 10, success value, current category id, and total questions. 
- Sample: `curl http://127.0.0.1:5000/categories/2/questions`
- Response:
    ``` {
      "category": "2",
      "questions": [
        {
          "answer": "Escher",
          "category": "2",
          "difficulty": 1,
          "id": 16,
          "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
        },
        {
          "answer": "Mona Lisa",
          "category": "2",
          "difficulty": 3,
          "id": 17,
          "question": "La Giaconda is better known as what?"
        },
        {
          "answer": "One",
          "category": "2",
          "difficulty": 4,
          "id": 18,
          "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
          "answer": "Jackson Pollock",
          "category": "2",
          "difficulty": 2,
          "id": 19,
          "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        }
      ],
      "success": true,
      "total_questions": 23
    }
    ```

### `GET '/quizzes'`
- General:
    - This enpoint takes quiz category and previous question parameters.
    - Returns a random question within the given category,
    if provided, that is not one of the previous questions. 
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [6, 12], "quiz_category":{"id": 3, "type": "Geography"}'`
- Response:
    ``` {
      "questions": {
        "answer": "Lake Victoria",
        "category": "3",
        "difficulty": 2,
        "id": 13,
        "question": "What is the largest lake in Africa?"
      }
    }
    ```

### Documentation Example

`GET '/api/v1.0/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
