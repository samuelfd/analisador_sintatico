def arruma_tabela(arquivo):
	saida = open(arquivo, 'r')
	lista = saida.readlines()
  		    
	
	for i in range(len(lista)):
		lista[i] = lista[i].split('@')
		lista[i].remove('\n')

	

	tabela = open('tabela.txt','r')
	tabela = tabela.readlines()
	
	for i in range(len(tabela)):
		tabela[i] = tabela[i].split(',')
		lista[i].append(tabela[i][0])	

	
arruma_tabela('tabela1.txt')

