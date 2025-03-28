import socket
import threading

# 🔹 Création du socket client (IPv4, TCP)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


nickname = input("Choose your nickname:")

# 🔹 Fonction pour recevoir les messages du serveur
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message =='NICK': # Si le serveur demande un pseudo
                client.send(nickname.encode('ascii'))
            else: 
                print(message) # Affiche les messages reçus
        except:
            print("An error occured")
            client.close()
            break

# 🔹 Fonction pour envoyer des messages au serveur
def write():
    while True:
        message = input("")  
        if message.startswith("/quit"):
            client.send(f'{nickname} left the chat.'.encode('ascii'))
            client.close()
            break
        elif message.startswith("/list"):
            client.send("/list".encode('ascii'))
        elif message.startswith("/exit"):
            client.send(f"/exit".encode('ascii'))
        else:
            formatted_message = f'{nickname}: {message}'  # Formate le message avec le pseudo
            client.send(formatted_message.encode('ascii'))  # Envoi du message formaté

# 🔹 Création des threads pour recevoir et envoyer les messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()