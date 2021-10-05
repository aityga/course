import socket
import webbrowser

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))

print(socket.gethostbyname_ex(socket.gethostname()))
server.listen()

while True:
    user, adres = server.accept()

    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)

        if data == "youtube":
            webbrowser.open("https://www.youtube.com")
        if data == "google":
            webbrowser.open("https://www.google.com")
