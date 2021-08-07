def colors(text: str, color: int):
	print(f"\033[1;{color}m{text}\033[m")

correct = lambda text: colors(text, 32)
log = lambda text: colors(text, 34)
error = lambda text: colors(text, 31)
