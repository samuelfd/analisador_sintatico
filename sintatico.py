from arruma_tabelalex import *
import unicodedata
import re

def atribuicao(tokens, i):	
	if(tokens[i][3]=='['[IDENTIFICADOR]''):  
		i = i+1		
		if(tokens[i][0]=='='):
			i = i+1			
			if((tokens[i][3]=='['[IDENTIFICADOR]'')or(tokens[i][0]=='"') or (tokens[i][0]=='Samuel') ):
				i = i+1				
				if(tokens[i][0]==';'):		
					return i 
				else:
					i = erro(tokens, i, ";")
			elif((tokens[i][0]=='"')): 
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
			elif((tokens[i][0]=='\'')): 
				i = i+1				
				if((tokens[i][3]=='"') or (tokens[i][3]=='Samuel')):
					i = i+1					
					if((tokens[i][0]=='\'')):
						i = i+1						
						if(tokens[i][0]==';'):
							return i 
						else:
							i = erro(tokens, i, ";")
					else:
						i=erro(tokens, i, "\'")
			else:
				print "Essa atribuicao nao e valida, o erro encontra-se, na linha", tokens[i][1], "coluna", tokens[i][2]
				i = erro(tokens, i, tokens[i][0])
		else:
			i=erro(tokens, i, "=")

def declaracao(tokens, i):	
	if((tokens[i][0]=='int')or(tokens[i][0]=='char')or(tokens[i][0]=='float')):		
		i=i+1
		if(tokens[i][3]!='['[IDENTIFICADOR]''):  
			print 'O token na linha', tokens[i][1] ,'coluna', tokens[i][2], ' Nao e um identificador ! '
			i = erro(tokens, i,tokens[i][0])
		else: 
			return i

def demais_funcoes(tokens, i):	
	if(tokens[i][0]=='printf'):
		i=i+1
	elif(tokens[i][0]=='scanf'):
		i=i+1
	else: 
		i=erro(tokens, i, 'printf')
		i=erro(tokens, i, 'scanf')

def A(tokens,i):
	if tokens[i][0] == '(' or tokens[i][0] == '['[IDENTIFICADOR]'' :
		i = B(tokens,i)
		i = A_linha(tokens,i)
		return i
	else :
		i = erro(tokens, i, tokens[i][0])
def A_linha(tokens,i):
	if tokens[i][0] == '||':
		i=i+1
		i = B(tokens,i)
		i = A_linha(tokens,i)
		return i
	else :		
		return i
def B(tokens,i):	
		if tokens[i][0] == '(' or tokens[i][0] == '['[IDENTIFICADOR]'' :
			i = C(tokens,i)
			i = B_linha(tokens,i)
			return i
		else :
			i = erro(tokens, i, tokens[i][0])
def B_linha(tokens,i):
	if tokens[i][0] == '&&':
		i=i+1
		i = D(tokens,i)
		i = B_linha(tokens,i)
		return i
	else :		
		return
def D(tokens,i):
	if tokens[i][0] == '(' or tokens[i][0] == '['[IDENTIFICADOR]'' :
		i = E(tokens,i)
		i = D_linha(tokens,i)
		return i
	else :
		i = erro(tokens, i, tokens[i][0])
def D_linha(tokens,i):
	if tokens[i][0] == '<'  :
		i=i+1
		i = D_2linha(tokens,i)
		return i
	elif tokens[i][0] == '>' 
		i=i+1
		i = D_2linha(tokens,i)
		return i
	else		
		return i
def D_2linha(tokens,i):
	if tokens[i][0] == '=' :
		i=i+1
		i = E(tokens,i)
		i = D_2linha(tokens,i)
		return i
	else :		
		return i;
def E(tokens,i):
	if tokens[i][0] == '(' or tokens[i][0] == '['[IDENTIFICADOR]'' :
		i = E(tokens,i)
		i = D_linha(tokens,i)
		return i
	else :
		i = erro(tokens, i, tokens[i][0])
def E_linha(tokens,i):
	if tokens[i][0] == '==' 
		i=i+1
		i = F(tokens,i)
		i = E_linha(tokens,i)

	elif tokens[i][0] == '!=' :
		i=i+1
		i = F(tokens,i)
		i = E_linha(tokens,i)
	else :
		return i
def F(tokens,i):
	if tokens[i][0] == '(' or tokens[i][0] == '['[IDENTIFICADOR]'' :
		i = G(tokens,i)
		i = F_linha(tokens,i)
		return i
	else :
		i = erro(tokens, i, tokens[i][0])
def F_linha(tokens,i):
	if tokens[i][0] == '+' :
		i = i+1
		i = G(tokens,i)
		i = F_linha(tokens,i)
		return i
	else :
		return i
def G(tokens,i):
	if tokens[i][0] == '(' or tokens[i][0] == '['[IDENTIFICADOR]'' :
		i = H(tokens,i)
		i = G_linha(tokens,i)
		return i
	else :
		i = erro(tokens, i, tokens[i][0])
def G_linha(tokens,i):
	if tokens[i][0] == '*':
		i = i+1
		i = H(tokens,i)
		i = G_linha(tokens,i)
	else :
		return i
def H(tokens,i):
	if tokens[i][0] == '(' :
		i=i+1                        
		i=A(tokens, i)                        
		i=i+1
		if tokens[i][0] == ')' :
			return i
		else :
			i = erro(tokens, i, tokens[i][0])
	elif tokens[i][0] == '['[IDENTIFICADOR]'' :
		return i
	else :
		i = erro(tokens, i, tokens[i][0])
		
def expressao(tokens, i):
	i = A(tokens, i)
	return i

def erro(tokens, i, caractere):	
	if((caractere!=';')or(caractere!='{')or(caractere!='}')or(caractere!=')')or(caractere!='(')):
		print "Existe um erro na linha ", tokens[i][1], "coluna ", tokens[i][2], "você nao esqueceu esse caracter esqueceu o caractere", caractere
	else:
		print "Existe um erro na linha ", tokens[i][1], "coluna ", tokens[i][2], "Olhe esse token", caractere
	exit()	
	return i



