import os
import json
from firebase_admin import credentials
import firebase_admin

firebase_credentials_json = os.environ.get("FIREBASE_CREDENTIALS")

# Convertir la cadena JSON en un objeto Python
firebase_credentials_dict = json.loads(firebase_credentials_json)

# Crear el objeto de credenciales
cred = credentials.Certificate(firebase_credentials_dict)

# Inicializar la aplicación de Firebase con las credenciales
firebase_admin.initialize_app(cred, {'storageBucket': os.environ.get("STORAGE_LINK")})
