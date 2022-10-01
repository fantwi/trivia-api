import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from settings import TEST_DB_NAME, DB_USER, DB_PASS


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = TEST_DB_NAME
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            DB_USER, DB_PASS, 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # Data for testing successful creation of question
        self.new_question = {
            'question': 'Who was the US president in 2021',
            'answer': 'Joe Biden',
            'category': '4',
            'difficulty': '4',
        }

        # Data for testing successful search for questions
        self.search_term = {
            'searchTerm': 'clay'
        }

        # Data for testing unsuccessful search for questions
        self.search_term2 = {
            'searchTerm': ''
        }

        # Data for testing successfully geting questions to play the quiz
        self.quiz_data = {
            'previous_questions': [6, 12],
            'quiz_category': {
                'id': 3,
                'type': 'Geography'
            }
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    @DONE
    Write at least one test for each test for successful operation and for expected errors.
    """

    """
        Test getting all categories. This test should pass.
    """

    def test_get_all_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))

    """
        Test getting a specific category. This test should fail.
    """

    def test_404_get_all_categories(self):
        res = self.client().get('/categories/200')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    """
        Test getting paginated questions. This test should pass.
    """

    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(len(data['categories']))

    """
        Test requesting for an invalid page. This test should fail.
    """

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    """
        Test deleting a question. This test should pass.
    """

    def test_delete_question(self):
        res = self.client().delete('/questions/6')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 6).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 6)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertEqual(question, None)

    """
        Test 422 Unprocessable sent if question does not exist 
        when deleting a question. This test should fail.
    """

    def test_422_sent_if_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    """
        Test 404 resource not found sent if question id is invalid 
        when deleting a question. This test should fail.
    """

    def test_404_sent_if_question_does_not_exist(self):
        res = self.client().delete('/questions/asdfgh10')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    """
        Test the creation of a new question. 
        This test should pass. 
    """

    def test_create_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    """
        Test 405 if question creation is not allowed. 
        This test should fail.
    """

    def test_405_if_question_creation_not_allowed(self):
        res = self.client().post('/questions/50', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    """
        Test 400 bad request for question creation if no question is sent. 
        This test should fail.
    """

    def test_400_if_question_creation_not_allowed(self):
        res = self.client().post('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    """
        Test successfully searching for a question. 
        This test will pass.
    """

    def test_search_question(self):
        res = self.client().post('/questions/search', json=self.search_term)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    """
        Test 400 bad request if search term is empty. 
        This test will fail.
    """

    def test_400_sent_empty_search_term(self):
        res = self.client().post('/questions/search', json=self.search_term2)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    """
        Test successfully getting questions by category. 
        This test will pass.
    """

    def test_get_question_by_category(self):
        res = self.client().get('/categories/3/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['category'])

    """
        Test for 422 sent when getting question by invalid category id. 
        This test should fail.
    """

    def test_422_invalid_category(self):
        res = self.client().get('/categories/1000/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    """
        Test for successfully getting questions to play the quiz. 
        This test should pass.
    """

    def test_play_quiz(self):
        res = self.client().post('/quizzes', json=self.quiz_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

    """
        Test 422 unprocessable sent when empty json data is sent while
        playing the quiz. This test will fail.
    """

    def test_422_play_quiz_empty_data(self):
        res = self.client().post('/quizzes', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    """
        Test 400 bad request sent when no data is sent while playing the quiz. 
        This test will fail.
    """

    def test_400_play_quiz_no_data(self):
        res = self.client().post('/quizzes')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
