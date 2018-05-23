from Model.usr import UserModel
from werkzeug.security import safe_str_cmp
def authenticate(username,password):
    user=UserModel.find_user_by_name(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
      id=payload['identity']
      return UserModel.find_user_by_id(id)
