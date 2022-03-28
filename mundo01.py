def desafio001():
  print('Ola mundo! Vamos la ')


def desafio002(nome):
  print(f'Seja Bem-vindo,{nome}')


def desafio003():
  n1 = int(input('Digite um numero :'))
  n2 = int(input('Digite um numero :'))
  n3 = n1 + n2
  print(f' A soma de {n1} + {n2} e igual a {n3} ')



def desafio004(entrada):
  print(f'O tipo de dado informado : {type(entrada)}')
  


def desafio005(numero):
  antecessor = numero - 1
  sucessor = numero + 1
  return f' O numero informado foi {numero}, o seu antecessor e {antecessor}, e seu sucessor {sucessor}'


def desafio006(numero):
  dobro = numero * 2
  triplo = numero * 3
  raiz = numero ** (1/2)
  return f' O dobro do numero e {dobro}, e o seu triplo foi {triplo} e sua raiz quadrada foi {raiz}'

def desafio007(numero1, numero2):
  m = (numero1 + numero2) / 2
  return f' A media entre a nota do primeiro bismetre {numero1} e {numero2} e igual {m} pontos .'

def desafio008():
  medida = float(input('Uma distancia em metros :'))
  cm = medida * 100
  mn = medida * 1000
  return f' A media {medida}m corresponde a {cm}cm e {mn}mn .'

def desafio009():
  num = int(input('Digite um numero para ver sua tabuada :'))
  print (f' {num} x {1} = {num * 1}')
  print (f' {num} x {2} = {num * 2}')
  print (f' {num} x {3} = {num * 3}')
  print (f' {num} x {4} = {num * 4}')
  print (f' {num} x {5} = {num * 5}')
  print (f' {num} x {6} = {num * 6}')
  print (f' {num} x {7} = {num * 7}')
  print (f' {num} x {8} = {num * 8}')
  print (f' {num} x {9} = {num * 9}')
  print (f' {num} x {10} = {num * 10}')

def desafio010():
  real = float(input('Digite seu valor em dinheiro : R$ '))
  dolar = real / 3.27
  print(f' Com R${real} voce pode comprar U${dolar:.2f}')

def desafio011():
  largura = float(input('Largura da parede :'))
  altura = float(input('Altura da parede:'))
  area = largura * altura
  print(f'Sua parede tem a dimensao de {largura} x {altura} e sua area e de {area}m².')
  tinta = area / 2
  print(f'Para pintar essa parede você precisara {tinta}l de tinta.')


# calcula de porcetagme 10 * 5 / 100
def desafio012():
  preco = float(input('Qual e o preco do produto : R$')) 
  novo = preco - (preco * 5 / 100)
  return f' O produto custava {preco}R$, na promocao com o desconto de 5% vai custar {novo:.2f}R$ . '

def desafio013():
  preco = float(input('Seu salario atualmente : R$'))
  novo = preco + (preco * 15 / 100)
  return f' Um funcionario ganhava {preco:.2f}R$, com o aumento de 15% no seu salario agora e {novo:.2f}R$ . '

def desafio014():
  c = float(input('Informe a temperatura em °C: '))
  f = ((9 * c) / 5) + 32
  return f' A temperatura de {c}°C, corresponde a {f}°F !.'

def desafio015():
  dias = int(input('Quantos dias alugados : '))
  km = float(input('Quntos Km rodado : '))
  pago = (dias * 60) + (km * 0.15)
  return f' O total a pagar e de R${pago:.2f} . '
  
def desafio016():
  from math import trunc
  num = float(input('Digite um numero por favor : '))
  return f' O valor digitado foi {num}, e a sua porcao inteira e de {trunc(num)} '

def desafio017():
  from math import hypot
  co = float(input('Comprimento do cateto oposto :'))
  ca = float(input('Comprimento do acateo adjacente : '))
  hi = hypot(co, ca)
  return f' A hipotenusa vai medir {hi:.2f} .'

def desafio018():
  from math import radians, sin, cos, tan
  angulo = float(input('Digite o angulo que para descobrir seno ,cosseno,tangente:'))
  seno = sin(radians(angulo))
  print(f' O angulo de {angulo} tem o SENO de {seno:.2f}. ')
  cosseno = cos(radians(angulo))
  print(f' O angulo de {angulo} tem o COSSENO de {cosseno:.2f}.')
  tangente = tan(radians(angulo))
  print(f' O angulo e de {angulo} tem o TANGENTE de {tangente:.2f}.')

def desafio019():
  from random import choice
  n1 = str(input('Primeiro aluno da classe :'))
  n2 = str(input('Segundo aluno da classe : '))
  n3 = str(input('Terceiro aluno da classe :'))
  n4 = str(input('Quarto aluno da classe :'))
  lista = [n1, n2, n3, n4, ]
  escolhido = choice(lista)
  print(f' O aluno escolhido para apagar o quadro foi{escolhido}. ')

def desafio020():
  from random import shuffle
  nome1 = str(input('Primeiro aluno:'))
  nome2 = str(input('Segundo aluno :'))
  nome3 = str(input('Terceiro aluno :'))
  nome4 = str(input('Quarto aluno :'))
  ordem = [nome1, nome2, nome3, nome4]
  shuffle(ordem)
  print('A Ordem de apresentacao sera :')
  print(ordem)

def desafio021():
  pass

def desafio022():
  nome = str(input('Seu Nome completo por favor : ')).strip()
  print('Analisando seu Nome :) ....')
  print(f' Seu nome em maiusculos e {nome.upper()} ')
  print(f' Seu nome em minusculo e {nome.lower()} ')
  print(f' Seu nome completo tem {len(nome)-nome.count(nome)} ')
  separa = nome.split()
  print(f' Seu primeiro nome e {(separa[0])} e ele tem {len(separa[0])} letras ')

def desafio023():
  num = int(input('Poderia me informar um numero : '))
  u = num // 1 % 10
  d = num // 10 % 10
  c = num // 100 % 10
  m = num // 1000 % 10
  print( f' Fazendo uma analise do numero {num} ')
  print( f' Sua Unidade : {u} ')
  print( f' Sua Dezena : {d} ')
  print( f' Sua Centena : {c} ')
  print( f' Sua Milhar : {m} ')

def desafio024():
  cidade = str(input('Qual cidade voce nasceu ? ')).strip()
  c_r = cidade[0:5].upper() == 'SANTO'
  print(f'Sua cidade tem santo no nome ? {c_r} ')

def desafio025():
  nome = str(input('Digite seu nome completo : ')).strip()
  n_r =  'SILVA' in nome.upper()
  print(f'Seu nome tem Silva ? {n_r} ')

def desafio026():
  frase = str(input('Digite uma frase bem interessante : ')).upper().strip()
  resul = frase.count('A')
  print(f' A letra A aparece {resul} vezes ! ')
  aparece = frase.find('A') + 1
  print(f' A letra A apareceu na posicao {aparece} ! ')
  ultima = frase.rfind('A') + 1
  print(f' A ultima letra A apareceu na posicao {ultima} ! ' )

def desafio027():
  n = str(input('Seu nome por favor : ')).strip()
  nome = n.split()
  print('Muito prazer em te conhecer :) !')
  print( f' Seu primeiro nome e {nome[0]} ')
  print( f' Seu ultimo nome e {nome[len(nome) -1]} ')

def desafio028():
  from random import randint
  from time import sleep 
  computador = randint(0,5) # Faz o computador 'PENSAR'
  print('-=-' * 10)
  print('Vou Pensar em um numero entre 0 e 5 . Tente adinvinhar ...')
  print('-=-' * 10)
  jogador = int(input('Em que numero eu pensei ? ')) # Jogador tentando adinvinhar
  print('Processando ...')
  sleep(4)
  if jogador == computador :
    print('PARABENS , Voce conseguir me vencer !')
  else:
    print(f' GANHEI , Eu pensei no numero {computador} e nao no {jogador} ')

def desafio029():
  velocidade = float(input('Qual e a Velocidade atual do Carro ? '))
  if velocidade > 80 :
    print('MULTADO! Voce execedeu o limite permitido que de 80km/h.')
    multa = (velocidade-80) * 7
    print(f'Voce deve pagar uma multa de {multa:.2f}R$ ! ')
  print('Tenha um Bom dia ! Dirija com Seguranca. ')

def desafio030():
  n1 = int(input('Me diga um numero qualquer : '))
  resultado = n1 % 2
  if resultado == 0 :
    print(f'O numero {n1} e PAR !')
  else:
    print(f'O numero {n1} e IMPAR !')

def desafio031():
  distancia = float(input('Qual e a distancia da sua viagem ? '))
  print(f'Voce esta prester a comeca uma viagem de {distancia}KM.')
  if distancia <= 200:
    preco = distancia * 0.50 
  else:
    preco = distancia * 0.45
  print(f'E o preco da passagem sera de {preco:.2f}R$.')

def desafio032():
  from datetime import date
  ano = int(input('Que ano quer Analisar ? Coloque 0 para analisar o ano atual : '))
  if ano == 0 :
    ano = date.today().year
  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} e BISSEXTO.')
  else:
    print(f'O ano de {ano} NAO e BISSEXTO.')

def desafio033():
  a = int(input('Digite um numero : '))
  b = int(input('Digite um numero : '))
  c = int(input('Digite um numero : '))
  menor = a
  if b < a and b < c :
    menor = b
  if c < a and c < b :
    menor = c
  maior = a 
  if b > a and b > c :
    maior = b
  if c > a and c > b :
    maior = c
  print(f'O menor valor digitado foi {menor}')
  print(f'O maior valor digitado foi {maior}')


def desafio034():
  salario = float(input('Qual e o salario do funcionario ? R$'))
  if salario <= 1250 :
    novo = salario + (salario * 15 / 100)
  else:
    novo = salario + (salario * 10 / 100)
  print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora ')

def desafio035():
  print('-=-' * 10)
  print('Analisador de Triangulos... ')
  print('-=-' * 10)
  r1 = float(input('Primeiro Segmento : '))
  r2 = float(input('Segundo Segmento : '))
  r3 = float(input('Terceiro Segmento : '))
  if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print('Os segmentos acima PODEM FORMA UM TRIANGULO !')
  else:
    print('Os segmentos acima NAO PODEM FORMA UM TRIANGULO !')














  



























