#!/usr/bin/python
# -*- coding: utf-8 -*-
#ver version de python instalada: python -ValueError
#pip install python-nmap
#from nmap import *, importa todas las clases y metodos del Modulo nmap

import nmap # import nmap.py module
#print help(nmap.PortScanner)
#print (nm.csv())

def escanear():
    Host = raw_input("Ingresa el Host: ")
    Port = raw_input("Ingresa el Puerto: ")
    escaneo = nmap.PortScanner()
    escaneo.scan(Host, Port)
    estado = escaneo[Host]["tcp"][int(Port)]["state"]
    version = escaneo[Host]["tcp"][int(Port)]["name"]
    target = escaneo[Host]["addresses"]["ipv4"]
    status_host = escaneo[Host]["status"]["state"]
    resultados = "[+] " + str(target)+ " " + str(status_host) + " " + str(version) + " " + str(estado)
    print resultados
escanear()
