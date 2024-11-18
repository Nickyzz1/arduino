import firebase_admin
from firebase_admin import credentials, firestore

# Inicialize o Firebase Admin SDK
cred = credentials.Certificate('caminho/para/seu/arquivo/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Acessando a base de dados Firestore
db = firestore.client()

def send_gps_to_firebase(latitude, longitude):
    # Criar um documento para armazenar as coordenadas
    gps_ref = db.collection('gps_data').document('robo_carga')

    # Atualizar as coordenadas no Firebase
    gps_ref.set({
        'latitude': latitude,
        'longitude': longitude
    })
    print(f"Coordenadas enviadas para o Firebase: {latitude}, {longitude}")
