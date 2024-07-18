from core.db.firebase_setup import db


def add_data(request):
    data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    db.child("users").push(data)
    return "push data successfully"


def get_data(request):
    users = db.child("users").get()
    user_list = users.val()
    return f"get_data{user_list}"
