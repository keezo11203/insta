from instagram_private_api import Client, ClientCompatPatch

# Replace the placeholders below with your actual Instagram credentials
username = 'user_name'
password = 'Password'

# Create an Instagram API client
api = Client(username, password)
api.login()

# Get your own user ID
my_user_id = api.authenticated_user_id

# Get the list of users you are following
rank_token = api.generate_uuid()
following = api.user_following(my_user_id, rank_token=rank_token)

# Get the list of users who are following you
followers = api.user_followers(my_user_id)

# Find unverified accounts that you are following and who don't follow you back
unverified_users = [
    user for user in following['users']
    if not user['is_verified'] and user['pk'] not in followers
]

# Unfollow unverified users who don't follow you back
for user in unverified_users:
    api.friendships_destroy(user['pk'])

print(f"Unfollowed {len(unverified_users)} unverified users who don't follow you back.")
