def A(tokens,i):
	if tokens[i][0] == '(' or tokens[i][0] == 'ID' :
		i = B(tokens,i)
		i = A_linha(tokens,i)
		return i
	else :
		erro()
def A_linha(tokens,i):
	if tokens[i][0] == '||':
		i=i+1
		i = B(tokens,i)
		i = A_linha(tokens,i)
		return i
	else :		
		return i
def B(tokens,i):	
		if tokens[i][0] == '(' or tokens[i][0] == 'ID' :
			i = C(tokens,i)
			i = B_linha(tokens,i)
			return i
		else :
			erro()
def B_linha(tokens,i):
	if tokens[i][0] == '&&':
		i=i+1
		i = D(tokens,i)
		i = B_linha(tokens,i)
		return i
	else :
		i=i+1
		return
def D(tokens,i):
	if tokens[i][0] == '(' or tokens[i][0] == 'ID' :
		i = E(tokens,i)
		i = D_linha(tokens,i)
		return i
	else :
		erro()
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
	if tokens[i][0] == '(' or tokens[i][0] == 'ID' :
		i = E(tokens,i)
		i = D_linha(tokens,i)
		return i
	else :
		erro()
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
	if tokens[i][0] == '(' or tokens[i][0] == 'ID' :
		i = G(tokens,i)
		i = F_linha(tokens,i)
		return i
	else :
		erro()
def F_linha(tokens,i):
	if tokens[i][0] == '+' :
		i = i+1
		i = G(tokens,i)
		i = F_linha(tokens,i)
		return i
	else :
		return i
def G(tokens,i):
	if tokens[i][0] == '(' or tokens[i][0] == 'ID' :
		i = H(tokens,i)
		i = G_linha(tokens,i)
		return i
	else :
		erro()
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
			erro()
	elif tokens[i][0] == 'ID' :
		return i
	else :
		erro()
               


		



def expressao(tokens, i): #expressão pode ser lógica, aritmetica ou um numeral 
	i = A(tokens, i)
	return i




