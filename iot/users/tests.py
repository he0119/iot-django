from collections import OrderedDict

from django.contrib.auth import get_user_model
from graphql_jwt.testcases import JSONWebTokenTestCase


# pylint: disable=no-member
class MeTests(JSONWebTokenTestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='test')
        self.client.authenticate(self.user)

    def test_get_user(self):
        query = '''
            query {
                me {
                    id
                    username
                }
            }
        '''

        variables = {
            'username': self.user.username,
        }

        result = self.client.execute(query, variables)
        # The user id will increase after each test
        # Do not assert id, it will vary based on the order that the test runner executes them.
        self.assertEqual(result.data['me']['username'], 'test')
        self.assertIsNone(result.errors)


class UnAuthMeTests(JSONWebTokenTestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='test')

    def test_get_user(self):
        query = '''
            query {
                me {
                    id
                    username
                }
            }
        '''

        variables = {
            'username': self.user.username,
        }

        result = self.client.execute(query, variables)
        self.assertIsNotNone(result.errors)
        self.assertEqual(result.data, OrderedDict([('me', None)]))


class UsersTests(JSONWebTokenTestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='test')
        self.client.authenticate(self.user)

    def test_get_user(self):
        query = '''
            query {
                users {
                    id
                    username
                }
            }
        '''

        variables = {
            'username': self.user.username,
        }

        result = self.client.execute(query, variables)
        self.assertEqual(len(result.data['users']), 1)
        self.assertIsNone(result.errors)
