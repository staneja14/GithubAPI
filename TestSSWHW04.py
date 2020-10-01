"""
This Python file contains code for testing SSWHW04
"""
import unittest
from SSWHW04 import getRepositories, getCommits, listOfRepositoriesWithCount


class TestSSWHW04(unittest.TestCase):
    def testgetRepositoriest(self):
        repos = getRepositories("staneja14")
        self.assertTrue(len(repos) > 0)
        self.assertIsNotNone(repos[0]['id'])

    def testGetCommits(self):
        commits = getCommits("staneja14", "Angular-Testing")
        self.assertTrue(len(commits) > 0)
        self.assertIsNotNone(commits[0]['sha'])

    def testlistOfRepositoriesWithCount(self):
        self.assertTrue("Repo: Angular-Testing Number of commits: 2" in listOfRepositoriesWithCount("staneja14"))
