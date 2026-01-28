
from backend.app import app, db, User

with app.app_context():
    users = User.query.all()
    print("Existing Users:")
    for u in users:
        print(f"Email: {u.email}, Is Admin: {u.is_admin}, City: {u.city}")
