from werkzeug.security import safe_str_cmp

from user import User

users = [
    User(1, "bob", "asdf")
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    #print(user)
    if user and safe_str_cmp(user.password, password):
        #print(user["password"])
        return user
#authenticate("bob","asdf")

def identity(payload):
    user_id = payload["identity"]
    #print(user_id)
    return userid_mapping.get(user_id, None)
#identity(payload)
