"""
Author: Shivani Taneja
This Python file contains code for Homework 04a of SSW567.

"""

import requests


def getRepositories(userID):
    """
    This function gets the list of all the repositories which a user has
    """
    repositories = requests.get('https://api.github.com/users/' + userID + '/repos')
    repositoryJson = repositories.json()
    return repositoryJson


def getCommits(userID, repositoryName):
    """

    :param userID: UserID of the Github User
    :param repositoryName: Repository Name for which we are fetching the number of commits
    :return: number of commits
    """
    repositories = requests.get('https://api.github.com/repos/' + userID + '/' + repositoryName + '/commits')
    repositoryJson = repositories.json()
    print(repositoryJson)
    return repositoryJson


def listOfRepositoriesWithCount(userID):
    """

    :param userID: UserID of the Github User
    :return: List of repositories with count of commits
    """
    result = ""
    repos = getRepositories(userID)
    for repo in repos:
        count = len(getCommits(userID, repo['name']))
        result += "Repo: " + repo['name'] + " Number of commits: " + str(count) + "\n"
        print("Repo : " + repo['name'] + " Number of commits: " + str(count))
    return result


# if __name__ == '__main__':
#     listOfRepositoriesWithCount("staneja14")