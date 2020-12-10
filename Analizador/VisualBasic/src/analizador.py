import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['MODULE','SUB','END','MOD','IMPORTS','PROGRAM','MAIN','ARGS','AS','STRING',
'CONSOLE','WRITELINE','VBCRLF','DIM','READLINE','DATETIME','NOW','READKEY','TRUE','FALSE'
		]

tokens = reservadas+['ID','NUMERO','SUMA','RESTA','DIV','MULTI','MENORQ','MAYORQ','IGUAL','NOIGUAL',
'PIZQ','PDER','LLIZQ','LLDER','PUNTO','UPDATE'
		]

t_ignore = '\t '
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTI = r'\*'
t_DIV = r'/'
t_IGUAL = r'='
t_MENORQ = r'<'
t_MAYORQ = r'>'
t_PIZQ = r'\('
t_PDER = r'\)'
t_PUNTO = r'\.'
t_NOIGUAL = '~='
t_LLIZQ = r'\{'
t_LLDER = r'\}'
t_UPDATE = r':='

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()		
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\'.*'
	pass

def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):	
	t.lexer.skip(1)

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs,files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		conteo = str(cont)
		conteo += ". "
		conteo += file
		print (conteo)

		cont = cont+1

	while respuesta == False:
		numArchivo = input("\nNumero del test: ")
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]


direccion ='C:/Users/Marco/Documents/test/'
archivi = buscarFicheros(direccion)
prueba = direccion+archivi
fp = codecs.open(prueba, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok : break
	print (tok)