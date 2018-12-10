#!/usr/bin/env python3
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channelStorage = connection.channel()
channelStorage.queue_declare(queue='StorageRequests')

channelEmailing = connection.channel()
channelEmailing.queue_declare(queue='EmailingRequests')

correos = "correo1@mail.com,correo2@mail.com"
print("nombre de archivo a subir:")
archivo = input()
channelStorage.basic_publish(exchange='',
                              routing_key='StorageRequests',
                                                    body=archivo)
channelEmailing.basic_publish(exchange='',
                              routing_key='EmailingRequests',
                                                    body=correos)
print(" Archivo enviado:", mensaje)
print(" Mensaje-e enviado a:", correos)
connection.close()

