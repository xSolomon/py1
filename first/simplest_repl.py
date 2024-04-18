'''
	Простейший REPL
'''

command : str = ''
while True:
	command = input('> ')
	if command == 'exit':
		break
	elif command == 'hello':
		print('Привет мир!')
	else:
		print(f'Неопознанная команда: {command}')
