#!/usr/bin/python3

from pyperclip import copy, paste
from subprocess import getoutput as rsh

LOCAL = '/sdcard/Tasker'

def print_colors(text, color=34):
	print(f"\033[1;{color}m{text}\033[m")

def main():
	print_colors(' Iniciando a sincronização...', 32)

	def get_clip():
		clip = rsh(f'adb shell cat {LOCAL}/.clip')
		return clip

	def send_clip(text: str):
		text_escaped = text.replace('"', r'\"').replace("'", r"\'")
		rsh(f"""adb shell 'echo "{text_escaped}" > {LOCAL}/.adb_clip'""")

	while True:
		old_system = paste()
		old_android = get_clip()

		while True:
			if old_system != paste():
				print_colors(' - Copia feita pelo computador...')
				send_clip(paste())
				break

			elif old_android != get_clip():
				if paste() != get_clip():
					print_colors(' - Copia feita pelo android...')
				copy(get_clip())
				break


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print_colors('\n Sincronização Parada!', 31)

