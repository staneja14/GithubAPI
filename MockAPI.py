from SSWHW04 import getRepositories
from SSWHW04 import getCommits
from SSWHW04 import listOfRepositoriesWithCount
import unittest
from unittest import mock
from mock import patch, Mock
import requests
import json


class FakeResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


switcher = {

    'https://api.github.com/users/staneja14/repos/GithubAPI/': 'data.json'

}


def mocked_requests_get(*args):
    if args[0] in switcher:
        with open(switcher[args[0]]) as f:
            return FakeResponse(json.load(f))
    return FakeResponse(None)


class TestRequestGitRepos(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def testrepository(self, mock_get):
        self.assertFalse(getRepositories('staneja14'), 'This is existing repository')

