def comandos(tokens, i):
	
	if(tokens[i][0]=='printf'):
		i=i+1
	elif(tokens[i][0]=='scanf'):
		i=i+1
	else: 
		i=erro(tokens, i, 'printf/scanf')