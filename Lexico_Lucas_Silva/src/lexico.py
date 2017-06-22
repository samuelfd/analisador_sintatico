#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from files import *
from erros import *
import re
from dicionario import *


def findTokens(source):
    i = 0
    linha = 1
    coluna = 1
    tokens = []
    tokenAux = ""

    while(i < len(source)):
        tokenAux += source[i]

        if (tokenAux == " "):  # Eliminar espaços
            tokenAux = ""
        else:

            if(tokenAux == '\n'):
                linha += 1
                coluna = 1
                tokenAux = ""

            if(tokenAux == '/'):   # verifica comentarios
                if(source[i + 1] == '/'):
                    tokenAux = ""
                    i += 1
                    while (source[i] != '\n'):
                        i += 1
                    else:
                        linha += 1
                        coluna = 1

                elif(source[i + 1] == '*'):  # ???
                    tokenAux = ""
                    i += 2
                    while (source[i] != '*' and source[i + 1] != '/'):
                        if(source[i] == '\n'):
                            linha += 1
                            coluna = 1
                        i += 1
                    else:
                        i += 2

            if(i + 1 < len(source)):
                if(re.match(r'^[a-zA-z0-9_]+$', tokenAux)):  # Pode ser um identificador ou uma palavra reservada.
                    if((source[i + 1] in delimitadores) or
                       (source[i + 1] in aritmeticos) or
                       (source[i + 1] in logicos) or
                       source[i + 1] == "\n"):
                        tokens.append([tokenAux, linha, coluna])
                        tokenAux = ""

                if(re.match(r'([-\d]+[.]*[\d]+)', tokenAux)):  # verifica numeros
                    if((source[i + 1] in delimitadores) or
                        (source[i + 1] in aritmeticos) or
                        (source[i + 1] in logicos) or
                       source[i + 1] == '\n'):
                        tokens.append([tokenAux, linha, coluna])
                        tokenAux = ""

                if(tokenAux == '='):    # verifica atribuição
                    if(re.match(r'([-\d]+[.]*[\d]+)', source[i + 1]) or
                       re.match(r'^[a-zA-z0-9_]+$', source[i + 1]) or
                       source[i + 1] == ' '):
                        tokens.append([tokenAux, linha, coluna])
                        tokenAux = ""

                if(tokenAux in delimitadores):  # verifica delimitadores
                    tokens.append([tokenAux, linha, coluna])
                    tokenAux = ""

                if(tokenAux in aritmeticos):  # verifica aritmeticos
                    tokens.append([tokenAux, linha, coluna])
                    tokenAux = ""

                if(tokenAux in logicos):  # verifica logicos
                    if(str(tokenAux + source[i + 1] in uniaoLogicos) or
                       source[i + 1] == ' ' or
                       source[i + 1] == r'([-\d]+[.]*[\d]+)' or
                       source[i + 1] == r'^[a-zA-z]+$'):

                    # Reconhecimento de dois simbolos logicos juntos
                    #    if(re.match(r'^[-0-9.]+$', source[i+1])):
                    #         tokens.append(tokenAux)
                    #         tokenAux = ""
                    #    else:
                    #        tokens.append(tokenAux + source[i+1])
                    #        tokenAux = ""
                    #        i += 1
                        tokens.append([tokenAux, linha, coluna])
                        tokenAux = ""
        coluna += 1
        i += 1

    for j in tokens:
        print j
    return tokens


def findErros(tokens):
    for lexema in tokens:
        # Encontrar identificadores errados
        if(re.match(r'([\d]+[a-zA-z_]+)', lexema[0])):
            setListaErros(getErro(02, lexema[1], lexema[2]))
        if(lexema[0] in logicos and
           ((tokens[tokens.index(lexema) + 1][0] in logicos) or
            (tokens[tokens.index(lexema) + 1][0] in aritmeticos)) and
            ((tokens[tokens.index(lexema) + 2][0] in logicos) or
             (tokens[tokens.index(lexema) + 2][0] in aritmeticos))):
            setListaErros(getErro(02, lexema[1], lexema[2]))

    for i in (getListaErros()):
        print i


def makeTable(tokens):
    for i in tokens:

        if (i[0] in reservadas):
            writeTable(['[RESERVADA]', i[1], i[2]])
            # print 'reservada'
            # break
        elif(i[0] in aritmeticos):
            writeTable(['[ARITM]', i[1], i[2]])
            # print 'arit'
            # break
        elif (i[0] in delimitadores):
            writeTable(['[DELIMITADOR]', i[1], i[2]])
            # print 'deli'
            # break
        elif(i[0] in logicos):
            writeTable(['[LOGICO]', i[1], i[2]])
            # print 'logicos'
            # br
        elif (re.match(r'^[-0-9.]+$', i[0])):
            writeTable(['[NUM]', i[1], i[2]])
            # print 'num'
            # break
        elif (re.match(r'^[a-zA-z0-9_]+$', i[0])):
            writeTable(['[IDENTIFICADOR]', i[1], i[2]])
            # print 'id'
            # break


def main():

    try:
        sys.argv[1]
    except Exception:
        print getErro(00, None, None)
        return None

    if(checarExtensao(sys.argv[1]) != 1):
        print getErro(01, None, None)
        return None

    source = readSource(sys.argv[1])  # Ler código fonte
    tokens = findTokens(source)      # Encontrar tokens
    findErros(tokens)                # Encontrar erros
    makeTable(tokens)                # Construir tabela de símbolos
    saida = open("tabela1.txt",'w')
    for i in tokens:
        for j in i:
            saida.write(str(j) + '@')
        saida.write('\n')
if __name__ == '__main__':
    main()
