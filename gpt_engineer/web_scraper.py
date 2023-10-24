import requests

from bs4 import BeautifulSoup


def push_changes(repo_path):
    """
    Push changes in a git repository to the remote repository. 

    This function uses the gitpython library to interact with the git repository. It first initializes a Repo object with the provided path, then gets a reference to the 'origin' remote. It then pushes the changes to the remote repository.

    Parameters
    ----------
    repo_path : str
        The local path of the git repository where changes should be pushed.

    Returns
    -------
    None
    """
    repo = git.Repo(repo_path)
    origin = repo.remote(name='origin')
    origin.push()