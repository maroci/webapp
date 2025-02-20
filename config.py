import os
db_host = os.environ.get('DB_HOST', default='localhost')
db_name = os.environ.get('DB_NAME', default='notes')
db_user = os.environ.get('DB_USERNAME', default='notes')
db_password = os.environ.get('DB_PASSWORD', default='')
db_port = os.environ.get('DB_PORT', default='5432')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

print("DEBUG: Database URI ->", SQLALCHEMY_DATABASE_URI)  # Add this line to check the URI

#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://demo:secure-password@54.170.97.218/sample')
#SQLALCHEMY_TRACK_MODIFICATIONS = False
