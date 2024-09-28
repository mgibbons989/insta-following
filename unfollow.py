import json
import os

path = os.getcwd()

def create_file(unfollow):
    name = '\\Unfollow_List.txt'
    file_path = path + name
    with open(file_path, 'w') as file:
        file.write("\n".join(unfollow))
    
    
with open(r'.\followers_1.json') as f:
    follower = json.load(f)

with open(r'.\following.json') as g:
    following = json.load(g)

followers_list = []
following_list = []

for i in follower:
    followers_list.append(i['string_list_data'][0]['value'])

for i in following['relationships_following']:
    following_list.append(i['string_list_data'][0]['value'])

followers_list.sort()
following_list.sort()

print(len(followers_list), len(following_list))

notfollowingback = []

for _ in range(len(following_list)):
    if following_list[_] not in followers_list:
        notfollowingback.append(following_list[_])

create_file(notfollowingback)