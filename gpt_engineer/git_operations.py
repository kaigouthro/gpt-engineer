   import subprocess

   def git_clone(repo_url, local_dir):
       subprocess.run(['git', 'clone', repo_url, local_dir])

   def git_pull(local_dir):
       subprocess.run(['git', '-C', local_dir, 'pull'])

   def git_commit(local_dir, message):
       subprocess.run(['git', '-C', local_dir, 'commit', '-m', message])

   def git_push(local_dir):
       subprocess.run(['git', '-C', local_dir, 'push'])