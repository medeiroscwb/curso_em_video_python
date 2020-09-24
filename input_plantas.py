class Planta:
    def __init__(self,nome,familia,genero,especie):
        self.nome = nome
        self.familia = familia
        self.genero = genero
        self.especie = especie

def mostrar_info(planta1):
    print('Nome Popular: ',planta1.nome)
    print('Família: ',planta1.familia)
    print('Gênero: ',planta1.genero)
    print('Espécie: ',planta1.especie)


planta1 = Planta('nome','familia','genero','especie')
planta1.nome = (input('Nome popular: '))
planta1.familia = (input('Família: '))
planta1.genero = (input('Gênero: '))
planta1.especie = (input('Especie: '))





'''nome = input('nome popular:')
   familia = input('Família:')
   genero = input('Gênero:')
   especie = input('Especie:')'''