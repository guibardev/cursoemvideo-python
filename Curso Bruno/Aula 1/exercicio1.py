nota1 = int(input('Digite a Nota 1:'))
nota2 = int(input('Digite a Nota 2:'))
media = (nota1 + nota2) / 2 
if media < 80:
    print('Você não passou de ano, a sua nota foi {}'.format(media)+ ' abaixo do requisitado')
if media >= 80:
    print('Você passou de ano, a sua nota foi{}'.format(media)+ ' acima do requisitado')