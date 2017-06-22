import unicodedata
import re
from arruma_tabelalex import *
from sintatico import *



i=0
while(tokens[i][3]=='$'):	
	if((tokens[i][0]=='int')or(tokens[i][0]=='float')or(tokens[i][0]=='char')):
		i = declaracao(tokens, i)	
	elif(tokens[i][2]=='['[IDENTIFICADOR]''):
		i = atribuicao(tokens, i)
	elif((tokens[i][0]=='scanf')or(tokens[i][0]=='printf')):
		i = demais_funcoes(tokens, i)
	else:
		erro(tokens, i, '')	
	i=i+1
	


print 'Nao foi encontrado erro no seu codigo!'

