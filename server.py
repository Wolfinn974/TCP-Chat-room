import socket
import threading
from datetime import datetime

# 🔹 Définition de l'adresse IP et du port du serveur
host = '127.0.0.1' #localhost
port = 55555

# 🔹 Création du socket serveur (IPv4, TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []
# 🔹 Fonction pour envoyer un message à tous les clients connectés
def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            client.send(message)

def handle(client):
    while True:
        try:
            message =  client.recv(1024).decode('ascii')
            timestamp = datetime.now().strftime('%H:%M:%S')
            formatted_message = f"[{timestamp}] {message}"

            if message.startswith("/list"):
                client.send("Connected users: ".encode('ascii') + ", ".join(nicknames).encode('ascii'))
            elif message.startswith("/exit"):
                index = clients.index(client)
                nickname = nicknames[index]
                clients.remove(client)
                nicknames.remove(nickname)
                client.close()
                broadcast(f"{nickname} has left the chat.".encode('ascii'))
                break
            else:
                broadcast(formatted_message.encode('ascii'), sender=client)
        except:
            # En cas de problème (déconnexion, erreur), suppression du client
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left the chat'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# 🔹 Fonction pour accepter et gérer les nouvelles connexions
def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode('ascii'))
        nickname =  client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print ('Nickname is {}'.format(nickname))
        broadcast('{} joined the chat'.format(nickname).encode('ascii'))
        client.send('Connected to server!' .encode('ascii'))

        # Création d'un thread pour gérer ce client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('The server is listening')
receive() # Démarrage du serveur
            