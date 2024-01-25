class Cachorro:
    def __init__(self,nome:str,idade:int,raca,albino=False):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.albino = albino
        if not isinstance(self.nome,str):
            raise TypeError ("o argumento nome precisa ser uma string")
        if not isinstance(self.idade,int):
            raise TypeError ("o argumento nome precisa ser um int")        
    def  latir(self):
        print("AuAu!")

    def morder(self,pessoa):
        print(f"{self.nome} mordeu {pessoa}")

#Adicionando Comentario para teste de commit com Branch
    def  latir_ingles(self):
        print("Woof!")
