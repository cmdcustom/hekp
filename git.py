import sys
import os
import pathlib
from github import Github

token = open('token.txt').read().replace('\n','')

auth = Github(token)

user = auth.get_user()

if sys.argv[1] == 'init':
    user.create_repo(sys.argv[2])
if sys.argv[1] == 'push':
    repo = user.get_repo(sys.argv[3])
    os.chdir(sys.argv[2])
    for file in os.listdir():
        repo.create_file(file, sys.argv[4], open(file).read())
   
