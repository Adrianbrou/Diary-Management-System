# decorators.py
from functools import wraps
import session_store


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session_store.current_user is None:
            print(" Please login first")
            return
        return func(*args, **kwargs)
    return wrapper
