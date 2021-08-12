#!/usr/bin/python3

from pyperclip import copy, paste
from subprocess import getoutput as rsh
from print_colors import error, correct, log

LOCAL = '/sdcard/Android/data/com.adb.clip.sync'

def main():
	correct(' Iniciando a sincronização...')

	def get_clip():
		clip = rsh(f'adb shell cat {LOCAL}/.clip')
		return clip

	def send_clip(text: str):
		text_escaped = text.replace('"', '\\"')
		rsh(f"""adb shell 'echo "{text_escaped}" > {LOCAL}/.adb_clip'""")

	while True:
		old_system = paste()
		old_android = get_clip()

		while True:
			if old_system != paste():
				log(' - Copia feita pelo computador...')
				send_clip(paste())
				break

			elif old_android != get_clip():
				if paste() != get_clip():
					log(' - Copia feita pelo android...')
				copy(get_clip())
				break

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		error('\n Sincronização Parada!')
