from dataclasses import dataclass
import sys




@dataclass
class User:
 '''
 classe que define o nome, aura, lista de amigos e lista de depoimentos de um valor a lista_user
 '''
 nome: str
 aura: int
 amigos: list[str]
 depoimentos: list[str]




#list_user será a lista principal que vai conter os valores User de todos os usuários
lista_user: list[User] = []




def main():
  '''
  A função principal, responsável por criar o menu e chamar as funções correspondentes ao número digitado pelo usuário.
  '''
  print('Aurium')
  print('1) Importar amizades de um arquivo')
  print('2) Criar usuário')
  print('3) Fazer amizade')
  print('4) Desfazer amizade')
  print('5) Fazer depoimento')
  print('6) Recomendações de amizade para um usuário')
  print('7) Ranking de aura')
  print('0) Sair')
  acao = input('Digite um número de ação! ')
  if int(acao) >= 1:
       if acao == '1':
           lista_nome = le_arquivo(input('Digite o nome do arquivo. '))
           converte(lista_nome)
           print()
       elif acao == '2':
           criar_usuario(input('Digite o nome do usuário. '))
           print()
       elif acao == '3':
           amigo1 = input('Digite o nome do usuário. ')
           amigo2 = input('Digite seu novo amigo. ')
           criar_amizade(amigo1 , amigo2)
           print()
       elif acao == '4':
           desf1 = input('Digite o nome do usuário. ')
           desf2 = input('Digite o nome de seu ex-amigo. ')
           desfazer(desf1, desf2)
           print()
       elif acao == '5':
           remet = input('Digite o remetente. ')
           dest = input('Digite o destinatário. ')
           depo = input('Digite o depoimento. ')
           depoimento(remet, dest, depo)
           print()
       elif acao == '67':
           print(lista_user)
           print()
       else:
           print('Número não atrelado a ação')
           print()
       main()
  else:
     print()
     print('Tchau!')
 
#AÇÃO 1
def le_arquivo(nome: str) -> list[list[str]]:
 '''
 Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é a
 lista de apelidos de uma linha (o primeiro é o da pessoa e os demais são os
 de seus amigos).
 Por exemplo, se o conteúdo do arquivo for
 Malbarbo Josiane Mauro Flavio
 Josiane Malbarbo
 a resposta produzida é
 [['Malbarbo', 'Josiane', 'Mauro', 'Flavio'], ['Josiane', 'Malbarbo']]
 '''
 try:
     with open(nome) as f:
         return [linha.split() for linha in f]
 except IOError as e:
     print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
     sys.exit(1)


'''
tem que ter uma função de erro entre a chamada do le_arquivo e do convert que diz se todos de uma lista de amigos existem como usuário
'''




def converte(nomes: list[list[str]]) -> None:
   """
   para cada nome da lista de nomes fornecida pela le_arquivo, essa função vai fazer uma lista de tipo user com o nome da pessoa, seus amigos,
   e aura e depoimentos sem valor no momento.




   >>> converte([['joao' , 'maria'] , ['maria' , 'joão']])
   [User('joão' , 0 , ['maria'] , []) , User('maria' , 0 , ['joão'] , [])]
   """
   lista: list[User] = []
   usuario: User = User('', 0, [], [])
   for _ in nomes:
       for __ in range(len(_)):
           if __ == 0:
               usuario = User(_[0], 0, [], [])
           else:
               usuario.amigos.append(_[__])
       lista.append(usuario)
   lista_user += lista




#AÇÃO 2
def criar_usuario(nome: str)-> None:
   '''
   recebe um *nome* e transforma essa string em um User( *nome* , 0 , [] , [])
   '''
   usuario: User = User(nome, 0, [], [])
   lista_user.append(usuario)




#AÇÃO 3
'''
tem que ter uma função que verifica se os usuários fazendo amizade existem na lista_user
'''
def criar_amizade(user1: str , user2: str)-> None:
   '''
   o user 1 vai ter o user 2 adicionado na lista de amigos e o user 2 vai ter o user 1 adicionado na sua lista de amigos. Ambos devem estar na
   lista_user. Ambos també recebem 100 pontos de aura
   '''
   for _ in lista_user:
       if user1 == _.nome:
           _.amigos.append(user2)
           _.aura += 100
   for __ in lista_user:
       if user2 == __.nome:
           __.amigos.append(user1)
           __.aura += 100




#AÇÃO 4
'''
função erro que verifica se os usuários são amigos
'''

def desfazer(user1: str , user2: str)-> None:
   '''
   Retira o user1 da lista de amigos do user2 e o user 2 da lista de amigos do user1. Além disso retira 150 pontos de aura de cada usuário




   pega a lista_user por índice, se esse índice tiver o mesmo nome ele pega a lista desse índice, procura o nome e arranca
   '''
   for _ in range(len(lista_user)):
       if lista_user[_].nome == user1:
           lista_user[_].aura -= 150
           for __ in range(len(lista_user[_].amigos)):
               if lista_user[_].amigos[__] == user2:
                   lista_user[_].amigos.pop(__)
   for x in range(len(lista_user)):
       if lista_user[x].nome == user2:
           lista_user[x].aura -= 150
           for y in range(len(lista_user[x].amigos)):
               if lista_user[x].amigos[y] == user1:
                   lista_user[x].amigos.pop(y)               




#AÇÃO 5
'''
função erro que verifica se os usuários são amigos

'''




def depoimento(remet: str, dest: str, depoi: str)-> None:
   '''
   após apontar o *rementente* e o *destinatário*, essa função salva um *depoimento* no usuário *destinatário*, adicionando 200 pontos para o
   *destinatário* e 50 para o *remetente*
   '''
   depcomp: str = 'De ' + remet + ': ' + depoi
   for i in range(len(lista_user)):
       if lista_user[i].nome == remet:
           lista_user[i].aura += 50
       if lista_user[i].nome == dest:
           lista_user[i].aura += 200
           lista_user[i].depoimentos.append(depcomp)


#AÇÃO 6
'''
função erro que diz se o mano é um usuário
'''
def recomendar(user: str)-> list[str]:
   '''
   RECOMENDAÇÃO: UMA LISTA DE AMIGOS DE AMIGOS DE UM CERTO USUÁRIO QUE NÃO SÃO AMIGOS
   parametro é só um usuário
   vai verificar a lista do usuário digitado
   '''








#AÇÃO 7






if __name__ == '__main__':
  main()
