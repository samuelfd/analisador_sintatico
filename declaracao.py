def declaracao(tokens, i):	
	if((tokens[i][0]=='int')or(tokens[i][0]=='char')or(tokens[i][0]=='float')):		
		i=i+1
		if(tokens[i][3]!='['[IDENTIFICADOR]''):  
			print 'O token na linha', tokens[i][1] ,'coluna', tokens[i][2], ' Nao e um identificador ! '
			i = erro(tokens, i,tokens[i][0])
		else: 
			return i

		i=i+1
		i = declaracao_linha(tokens, i)
		return i


