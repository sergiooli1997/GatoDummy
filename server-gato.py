#!/usr/bin/env python3

import socket
import time
import random
import os

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
buffer_size = 1024


def horizontal(tablero, n):
    server_win = 0
    client_win = 0
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == 'O':
                server_win += 1
            if tablero[i][j] == 'X':
                client_win += 1
        if n == 3 and client_win == 3:
            return 1
        if n == 3 and server_win == 3:
            return 2
        if n == 5 and client_win == 5:
            return 1
        if n == 5 and server_win == 5:
            return 2
        server_win = 0
        client_win = 0
    return 0


def vertical(tablero, n):
    server_win = 0
    client_win = 0
    for j in range(n):
        for i in range(n):
            if tablero[i][j] == 'O':
                server_win += 1
            if tablero[i][j] == 'X':
                client_win += 1
        if n == 3 and client_win == 3:
            return 1
        if n == 3 and server_win == 3:
            return 2
        if n == 5 and client_win == 5:
            return 1
        if n == 5 and server_win == 5:
            return 2
        server_win = 0
        client_win = 0
    return 0


def diagonal(tablero, n):
    server_win = 0
    client_win = 0
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == 'O' and i == j:
                server_win += 1
            if tablero[i][j] == 'X' and i == j:
                client_win += 1
    if n == 3 and client_win == 3:
        return 1
    if n == 3 and server_win == 3:
        return 2
    if n == 5 and client_win == 5:
        return 1
    if n == 5 and server_win == 5:
        return 2
    server_win = 0
    client_win = 0
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == 'O' and (i + j) == (n - 1):
                server_win += 1
            if tablero[i][j] == 'X' and (i + j) == (n - 1):
                client_win += 1
    if n == 3 and client_win == 3:
        return 1
    if n == 3 and server_win == 3:
        return 2
    if n == 5 and client_win == 5:
        return 1
    if n == 5 and server_win == 5:
        return 2
    return 0


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")
    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        count = 0
        print("Conectado a", Client_addr)
        while True:
            print("Esperando a recibir datos... ")
            data = Client_conn.recv(buffer_size)
            dificultad = int.from_bytes(data, byteorder='big')
            print("Recibido,", dificultad, "   de ", Client_addr)
            if dificultad == 1:
                tablero = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
                while True:
                    if horizontal(tablero, 3) == 0 and vertical(tablero, 3) == 0 and diagonal(tablero, 3) == 0:
                        Client_conn.sendall(bytes([0]))
                    if horizontal(tablero, 3) == 1 or vertical(tablero, 3) == 1 or diagonal(tablero, 3) == 1:
                        Client_conn.sendall(bytes([1]))
                        break
                    if horizontal(tablero, 3) == 2 or vertical(tablero, 3) == 2 or diagonal(tablero, 3) == 2:
                        Client_conn.sendall(bytes([2]))
                        break
                    data = Client_conn.recv(buffer_size)
                    x = int.from_bytes(data, "big")
                    data = Client_conn.recv(buffer_size)
                    y = int.from_bytes(data, "big")
                    tablero[x][y] = 'X'
                    print(tablero)
                    # determinar ganador
                    if horizontal(tablero, 3) == 0 and vertical(tablero, 3) == 0 and diagonal(tablero, 3) == 0:
                        Client_conn.sendall(bytes([0]))
                    if horizontal(tablero, 3) == 1 or vertical(tablero, 3) == 1 or diagonal(tablero, 3) == 1:
                        Client_conn.sendall(bytes([1]))
                        break
                    if horizontal(tablero, 3) == 2 or vertical(tablero, 3) == 2 or diagonal(tablero, 3) == 2:
                        Client_conn.sendall(bytes([2]))
                        break
                    count += 1
                    if count == 9:
                        break
                    else:
                        while True:
                            x_server = random.randint(0, 2)
                            y_server = random.randint(0, 2)
                            if tablero[x_server][y_server] == '-':
                                Client_conn.sendall(bytes([x_server]))
                                Client_conn.sendall(bytes([y_server]))
                                break
                            else:
                                print("Ocupado :c")
                        count += 1
                        print("Tiro Servidor")
                        tablero[x_server][y_server] = 'O'
                        print(tablero)
            if dificultad == 2:
                tablero = [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]
                while True:
                    if horizontal(tablero, 5) == 0 and vertical(tablero, 5) == 0 and diagonal(tablero, 5) == 0:
                        Client_conn.sendall(bytes([0]))
                    if horizontal(tablero, 5) == 1 or vertical(tablero, 5) == 1 or diagonal(tablero, 5) == 1:
                        Client_conn.sendall(bytes([1]))
                        break
                    if horizontal(tablero, 5) == 2 or vertical(tablero, 5) == 2 or diagonal(tablero, 5) == 2:
                        Client_conn.sendall(bytes([2]))
                        break
                    data = Client_conn.recv(buffer_size)
                    x = int.from_bytes(data, "big")
                    data = Client_conn.recv(buffer_size)
                    y = int.from_bytes(data, "big")
                    tablero[x][y] = 'X'
                    print(tablero)
                    # determinar ganador
                    if horizontal(tablero, 5) == 0 and vertical(tablero, 5) == 0 and diagonal(tablero, 5) == 0:
                        Client_conn.sendall(bytes([0]))
                    if horizontal(tablero, 5) == 1 or vertical(tablero, 5) == 1 or diagonal(tablero, 5) == 1:
                        Client_conn.sendall(bytes([1]))
                        break
                    if horizontal(tablero, 5) == 2 or vertical(tablero, 5) == 2 or diagonal(tablero, 5) == 2:
                        Client_conn.sendall(bytes([2]))
                        break
                    count += 1
                    if count == 25:
                        break
                    else:
                        while True:
                            x_server = random.randint(0, 4)
                            y_server = random.randint(0, 4)
                            if tablero[x_server][y_server] == '-':
                                Client_conn.sendall(bytes([x_server]))
                                Client_conn.sendall(bytes([y_server]))
                                break
                            else:
                                print('Ocupado')
                        count += 1
                        print("Tiro Servidor")
                        tablero[x_server][y_server] = 'O'
                        print(tablero)
            break
