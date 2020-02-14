#!/usr/bin/env python3

import socket
import os
from time import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
buffer_size = 1024


def imprimir_tablero(tablero, n):
    a = ""
    if n == 3:
        print('\t0' + '\t1' + '\t2')
    if n == 5:
        print('\t0' + '\t1' + '\t2' + '\t3' + '\t4')
    for i in range(n):
        print(i, end="\t")
        for j in range(n):
            a += str(tablero[i][j]) + '\t'
        print(a)
        a = ""


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
    count = 0
    bandera = 0
    tiempo_inicial = time()
    print("------Bienvenido al Gato Dummy------")
    print("Elige dificultad ;)")
    print("1.- Dificultad principiante")
    print("2.- Dificultad avanzada")
    dificultad = int(input())
    TCPClientSocket.sendall(bytes([dificultad]))
    if dificultad == 1:
        tablero = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        imprimir_tablero(tablero, 3)
        while True:
            os.system('cls')
            data = TCPClientSocket.recv(buffer_size)
            bandera = int.from_bytes(data, "big")
            if bandera == 0:
                pass
            else:
                data = TCPClientSocket.recv(buffer_size)
                print('Finalizado.')
                imprimir_tablero(tablero, 3)
                if bandera == 1:
                    print('Ganaste :D Buen juego')
                else:
                    print('Perdiste :( ')
                break
            while True:
                x = int(input())
                y = int(input())
                if tablero[x][y] == '-':
                    TCPClientSocket.sendall(bytes([x]))
                    TCPClientSocket.sendall(bytes([y]))
                    break
                else:
                    print("Casilla Ocupada :C")
            tablero[x][y] = 'X'
            imprimir_tablero(tablero, 3)
            data = TCPClientSocket.recv(buffer_size)
            bandera = int.from_bytes(data, "big")
            if bandera == 0:
                pass
            else:
                print('Finalizado.')
                imprimir_tablero(tablero, 3)
                if bandera == 1:
                    print('Ganaste :D Buen juego')
                else:
                    print('Perdiste :( ')
                break
            count += 1
            if count == 9:
                print('Empate :o')
                break
            else:
                data = TCPClientSocket.recv(buffer_size)
                x_server = int.from_bytes(data, "big")
                data = TCPClientSocket.recv(buffer_size)
                y_server = int.from_bytes(data, "big")
                tablero[x_server][y_server] = 'O'
                count += 1
                print("El servidor eligio")
                imprimir_tablero(tablero, 3)
    if dificultad == 2:
        tablero = [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]
        imprimir_tablero(tablero, 5)
        while True:
            os.system('cls')
            data = TCPClientSocket.recv(buffer_size)
            bandera = int.from_bytes(data, "big")
            if bandera == 0:
                pass
            else:
                data = TCPClientSocket.recv(buffer_size)
                print('Finalizado.')
                imprimir_tablero(tablero, 5)
                if bandera == 1:
                    print('Ganaste :D Buen juego')
                else:
                    print('Perdiste :( ')
                break
            while True:
                x = int(input())
                y = int(input())
                if tablero[x][y] == '-':
                    TCPClientSocket.sendall(bytes([x]))
                    TCPClientSocket.sendall(bytes([y]))
                    break
                else:
                    print("Casilla Ocupada :C")
            tablero[x][y] = 'X'
            imprimir_tablero(tablero, 5)
            data = TCPClientSocket.recv(buffer_size)
            bandera = int.from_bytes(data, "big")
            if bandera == 0:
                pass
            else:
                print('Finalizado.')
                imprimir_tablero(tablero, 5)
                if bandera == 1:
                    print('Ganaste :D Buen juego')
                else:
                    print('Perdiste :( ')
                break
            count += 1
            if count == 25:
                print('Empate :o')
                break
            else:
                data = TCPClientSocket.recv(buffer_size)
                x_server = int.from_bytes(data, "big")
                data = TCPClientSocket.recv(buffer_size)
                y_server = int.from_bytes(data, "big")
                tablero[x_server][y_server] = 'O'
                count += 1
                print("El servidor eligio")
                imprimir_tablero(tablero, 5)
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print('Duracion de la partida:',end="")
    print(tiempo_ejecucion)