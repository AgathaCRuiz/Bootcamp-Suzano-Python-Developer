class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def pedalar(self):
        print("Vrummmm...")

    def trocar_marcha(self, nmr_marcha):
        print("Trocando marcha...")
        if nmr_marcha > self.marcha:
            print("Marcha trocada!")
            self.marcha = nmr_marcha
        else:
            print("Não é possível trocar marcha")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

# Teste
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.pedalar()
b1.parar()
print(b1.cor)

# Criando outra bicicleta
b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)

b2.trocar_marcha(3)
print(b2)
