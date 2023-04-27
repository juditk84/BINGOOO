import random

class jugador():
    
    def __init__(self, name):
        self.name = name
        self.cartro = None #he intentat inicialitzar el cartró fent self.cartro = OmplirCartro()
                           #però no va, surely i'm missing something here. Crec que molaria poder
                           #inicialitzar el cartró desde el constructor i tenir-lo ja omplert sense
                           #haver de fer instancia.OmpliCartro(), saps?
                           #igual directament no estic pillant la lògica del __init__ jsjsjsj
    
    def OmplirCartro(self):
        
        cartro = []

        num_boletes = 15

        while num_boletes > 0:
            
            boleta = (random.randint(1, 90))

            if boleta not in cartro:
                cartro.append(boleta)
                num_boletes -= 1
            else:
                pass
        
        self.cartro = cartro

    def Comprovar(self, boleta):

        if boleta in self.cartro:
            self.cartro.remove(boleta)

        print(f"El cartró del jugador {self.name} queda així:\n{self.cartro}")
