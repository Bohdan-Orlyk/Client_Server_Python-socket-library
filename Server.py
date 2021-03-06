import socket
from Terminal import *

host = "127.0.0.1"
port = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((host, port))
    server.listen(4)

    print("SERVER STARTED!")

    while True:
        user, address = server.accept()

        with user:
            print(f"Connected by {address}")

            while True:
                option = user.recv(1024).decode('utf-8')
                print("Option:", option)

                if option == '1':
                    try:
                        create_user(user)
                    except ConnectionRefusedError:
                        request_to_client(user, "Cos poszlo nie tak :( ")
                        print("ERROR!")

                elif option == '2':
                    try:
                        change_balance(user)
                    except ConnectionRefusedError:
                        request_to_client(user, "Cos poszlo nie tak :( ")
                        print("ERROR!")

                    except FileNotFoundError:
                        request_to_client(user, "Nieprawidlowo podane dane!")
                        print("ERROR!")

                    except ValueError:
                        request_to_client(user, "Nieprawidlowo podane dane!")
                        print("ERROR!")

                elif option == '3':
                    try:
                        show_information(user)
                    except ConnectionRefusedError:
                        request_to_client(user, "Cos poszlo nie tak :( ")
                        print("ERROR!")

                    except FileNotFoundError:
                        request_to_client(user, "Nieprawidlowo podane dane!")
                        print("ERROR!")

                elif option == '4':
                    try:
                        get_money(user)
                    except ConnectionRefusedError:
                        request_to_client(user, "Cos poszlo nie tak :( ")
                        print("ERROR!")

                    except FileNotFoundError:
                        request_to_client(user, "Nieprawidlowo podane dane!")
                        print("ERROR!")

                    except ValueError:
                        request_to_client(user, "Nieprawidlowo podane dane!")
                        print("ERROR!")

                if not option:
                    print('USER DISCONNECTED!')
                    break
