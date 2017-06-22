def erro(tokens, i, caractere):	
	if((caractere!=';')or(caractere!='{')or(caractere!='}')or(caractere!=')')or(caractere!='(')):
		print "Existe um erro na linha ", tokens[i][1], "coluna ", tokens[i][2], "você nao esqueceu esse caracter esqueceu o caractere", caractere
	else:
		print "Existe um erro na linha ", tokens[i][1], "coluna ", tokens[i][2], "Olhe esse token", caractere
	exit()	
	return i