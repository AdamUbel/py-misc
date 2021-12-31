import functools

user = {"username": "jose", "access_level": 0}

def make_secure(access_level, level_name):
  def decorator(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
      if user["access_level"] >= access_level:
        return func(*args, **kwargs)
      elif  user["access_level"] < access_level:
        return f"No {level_name} permissions for {user['username']}"

    return secure_function
  
  return decorator

@make_secure(2, "admin")
def get_password():
  return f"admin {user['username']}: 1234"


@make_secure(1, "user")
def get_dashboard_password():
  return f"user {user['username']}: user_password"

print(get_password())
print(get_dashboard_password())


user = {"username": "ann", "access_level": 2}

print(get_password())
print(get_dashboard_password())

user = {"username": "beth", "access_level": 1}

print(get_password())
print(get_dashboard_password())