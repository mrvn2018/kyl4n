#!/usr/bin/python
# -*- coding: utf-8 -*-
#Este script realiza el escaneo simple de un puerto con nmap

import nmap # importar modulo nmap.py 

def escanear():
    Host = raw_input("Ingresa el Host: ")
    Port = raw_input("Ingresa el Puerto: ")
    escaneo = nmap.PortScanner()
    escaneo.scan(Host, Port)
    estado = escaneo[Host]["tcp"][int(Port)]["state"]
    version = escaneo[Host]["tcp"][int(Port)]["name"]
    target = escaneo[Host]["addresses"]["ipv4"]
    status_host = escaneo[Host]["status"]["state"]
    resultados = "[+] " + str(target)+ "        " + str(status_host) + "           " + str(version) + "      " + str(estado)
    print ("    Target      " + "Estado del Host  " + "Version " + " " + "Estado del Puerto ")
    print resultados
escanear()
