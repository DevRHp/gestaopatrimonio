
from backend.app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # 1. Update/Create Super Admin (admin@123)
    super_admin = User.query.filter_by(email='admin@123').first()
    if not super_admin:
        super_admin = User(email='admin@123', city='Sorocaba', is_admin=True)
        db.session.add(super_admin)
        print("Created user admin@123")
    
    super_admin.password = generate_password_hash('Marionete12') # Updated pass
    super_admin.is_admin = True
    print("Set password for admin@123 to 'Marionete12'")

    # 2. Update/Create Dev Admin (devprudencio@gmail.com)
    dev_admin = User.query.filter_by(email='devprudencio@gmail.com').first()
    if not dev_admin:
        dev_admin = User(email='devprudencio@gmail.com', city='Sorocaba', is_admin=True)
        db.session.add(dev_admin)
        print("Created user devprudencio@gmail.com")
    
    dev_admin.password = generate_password_hash('Rafarhp1512')
    dev_admin.is_admin = True
    print("Set password for devprudencio@gmail.com to 'Rafarhp1512'")
    
    db.session.commit()
    print("Database updated successfully.")
