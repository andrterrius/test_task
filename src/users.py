from werkzeug.security import generate_password_hash
users = {'recruto': {'password': generate_password_hash('recruto password')}}