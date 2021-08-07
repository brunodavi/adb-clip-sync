#!/usr/bin/python3

from subprocess import getoutput as rsh
from print_colors import error, correct, log
from re import findall

adb = lambda cmd: rsh(f'adb -d {cmd}')
devices = findall('(.+)\t+device', adb('devices'))
ips = findall('addr:(\S+)', adb('shell ifconfig wlan0'))

if not (ips and devices):
	error('Erro ao executar o adb')
	exit()

tcpip = f'{ips[0]}:5555'

if ips and devices and tcpip not in devices:
	out = adb(f'connect {tcpip}')

	if 'Connection refused' in out:
		adb('tcpip 5555')
		log('Reexecute para se conectar')

	else:
		correct(out)

else:
	out = adb(f'disconnect {tcpip}')
	error(out)
