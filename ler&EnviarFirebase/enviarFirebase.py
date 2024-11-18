import serial
import time
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializando o Firebase Admin SDK
cred = credentials.Certificate('caminho/para/seu/arquivo/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Acessando a base de dados Firestore
db = firestore.client()

# Configuração da porta serial para o GPS
serial_port = '/dev/ttyS0'  # Porta serial do Raspberry Pi
baud_rate = 9600  # Taxa de transmissão do GPS

# Inicializando a comunicação serial com o módulo GPS
ser = serial.Serial(serial_port, baud_rate)

# Função para enviar as coordenadas para o Firebase
def send_gps_to_firebase(latitude, longitude):
    gps_ref = db.collection('gps_data').document('robo_carga')
    gps_ref.set({
        'latitude': latitude,
        'longitude': longitude
    })
    print(f"Coordenadas enviadas para o Firebase: Latitude: {latitude}, Longitude: {longitude}")

# Função para obter as coordenadas GPS
def get_gps_data():
    while True:
        data = ser.readline().decode('utf-8', errors='ignore')  # Lê a linha de dados do GPS

        print(data)  # Exibe os dados no terminal para depuração

        # Se a linha contiver as informações de localização (por exemplo, "$GPGGA")
        if '$GPGGA' in data:
            parts = data.split(',')
            try:
                latitude = parts[2]  # A latitude está na posição 2
                longitude = parts[4]  # A longitude está na posição 4
                print(f"Latitude: {latitude}, Longitude: {longitude}")

                # Enviar as coordenadas para o Firebase
                send_gps_to_firebase(latitude, longitude)

            except IndexError:
                pass  # Em caso de dados incompletos, ignora

        time.sleep(1)  # Intervalo para ler os dados novamente

# Inicia o processo de leitura e envio de dados
get_gps_data()
