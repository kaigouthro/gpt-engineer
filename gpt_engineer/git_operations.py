import subprocess

def git_clone(repo_url, local_dir):
    """
    Clone a git repository to a local directory.

    Args:
        repo_url (str): The URL of the git repository to clone.
        local_dir (str): The local directory where the repository should be cloned.
    """
    subprocess.run(['git', 'clone', repo_url, local_dir])

def git_pull(local_dir):
    """
    Pull the latest changes from a git repository.

    Args:
        local_dir (str): The local directory where the repository is located.
    """
    subprocess.run(['git', '-C', local_dir, 'pull'])

def git_commit(local_dir, message):
    """
    Commit changes to a git repository with a specific message.

    Args:
        local_dir (str): The local directory where the repository is located.
        message (str): The commit message.
    """
    subprocess.run(['git', '-C', local_dir, 'commit', '-m', message])

def git_push(local_dir):
    """
    Push committed changes to a git repository.

    Args:
        local_dir (str): The local directory where the repository is located.
    """
    subprocess.run(['git', '-C', local_dir, 'push'])