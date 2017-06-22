def atribuicao(tokens, i):	
	if(tokens[i][3]=='['[IDENTIFICADOR]''): # o que quer dizer que um identificador 
		i = i+1		
		if(tokens[i][0]=='='): # está recebendo um valor
			i = i+1			
			if((tokens[i][3]=='['[IDENTIFICADOR]'')or(tokens[i][0]=='"') or (tokens[i][0]=='Samuel') ):#atribui
				#i = expressao(tokens, i)
				i = i+1				
				if(tokens[i][0]==';'):		
					return i 
				else:
					i = erro(tokens, i, ";")
			elif((tokens[i][0]=='"')): # quando estou recebendo um literal x = "a"
				i = i+1				
				if((tokens[i][3]=='"') or (tokens[i][3]=='Samuel')):
					i = i+1					
					if((tokens[i][0]=='"')):
						i = i+1						
						if(tokens[i][0]==';'):
							return i 
						else: 
							i = erro(tokens, i, ";")
					else:
						i=erro(tokens, i, "\"")
			elif((tokens[i][0]=='\'')): # quando estou recebendo um literal x = "a"
				i = i+1				
				if((tokens[i][3]=='"') or (tokens[i][3]=='Samuel')):
					i = i+1					
					if((tokens[i][0]=='\'')):
						i = i+1						
						if(tokens[i][0]==';'):
							return i 
						else:i = erro(tokens, i, ";")
					else:i=erro(tokens, i, "\'")
			else:
				print "Você está tentando fazer uma atribuição de um token não válido, na linha", aux[0], "coluna", aux[1]
				i = erro(tokens, i, tokens[i][0])
		else:
			i=erro(tokens, i, "=")
