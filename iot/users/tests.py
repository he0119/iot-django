from collections import OrderedDict

from django.contrib.auth import get_user_model
from graphql_jwt.testcases import JSONWebTokenTestCase


# pylint: disable=no-member
class UsersTests(JSONWebTokenTestCase):
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
        self.assertEqual(
            result.data,
            OrderedDict(
                [('me', OrderedDict([('id', '1'), ('username', 'test')]))]
            )
        )
        self.assertIsNone(result.errors)


class UnAuthUsersTests(JSONWebTokenTestCase):
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
