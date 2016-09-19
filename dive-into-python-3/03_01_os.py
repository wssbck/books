import os

# get current working directory
print(os.getcwd())

# get user's home directory
user_path = os.path.expanduser('~')
print(user_path)

# print full current path
print(os.path.realpath('.'))

# experiment with path joining
print(os.path.join(user_path, user_path))