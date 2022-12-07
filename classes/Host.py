import os
import platform
import re
import socket
import uuid

import psutil as psutil


class Host:
    def __init__(self):
        self.username = os.environ.get('USER', os.environ.get('USERNAME'))
        self.hostname = platform.node()
        self.os = platform.platform()
        self.architecture = platform.architecture()
        self.local_ip = socket.gethostbyname(socket.gethostname())
        # self.external_ip = get('https://api.ipify.org').content.decode('utf8')
        self.mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        self.ram = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
        # self.cpu = str(psutil.cpu_freq().max / 1000) + " GHz" + ", " + str(cpuinfo.get_cpu_info()['brand_raw'])

    def __str__(self) -> str:
        return "Username: " + self.username + "\n" + \
               "Hostname: " + self.hostname + "\n" + \
               "OS: " + self.os + "\n" + \
               "Architecture: " + str(self.architecture) + "\n" + \
               "Local IP: " + self.local_ip + "\n" + \
               "MAC: " + self.mac + "\n" + \
               "RAM: " + self.ram + "\n"
        # "CPU: " + self.cpu
        # "External IP: " + self.external_ip + "\n" + \

    def to_json(self):
        return {"username": self.username,
                "hostname": self.hostname,
                "os": self.os,
                "architecture": self.architecture,
                "local_ip": self.local_ip,
                "mac": self.mac,
                "ram": self.ram,
                }
