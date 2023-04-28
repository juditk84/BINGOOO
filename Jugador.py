import random

'''
Val, aquí no sé què dir-te. Si seguim el que diu l'enunciat, està malament, perquè es demana crear dues funcions, no una classe.
Recorda que la idea és aprendre a fer anar bé les funcions primer, i després passar a classes, que és un nivell d'abstracció més alt.

Per altra banda, la classe Jugador té tot el sentit del món, l'ha detectada correctament i has posat uns mètodes a dins que tenen sentit.
'''
class jugador(): # Noms de les classes en majúscules, per conveni. Així distingim què és una classe i què és un objecte de la classe a simple vista.
    
    def __init__(self, name):
        self.name = name
        # Has provat self.cartro = self.OmplirCartro()?
        self.cartro = None #he intentat inicialitzar el cartró fent self.cartro = OmplirCartro()
                           #però no va, surely i'm missing something here. Crec que molaria poder
                           #inicialitzar el cartró desde el constructor i tenir-lo ja omplert sense
                           #haver de fer instancia.OmpliCartro(), saps?
                           #igual directament no estic pillant la lògica del __init__ jsjsjsj
    
    def OmplirCartro(self):
        
        cartro = []

        num_boletes = 15

        while num_boletes > 0: # Molt bé la forma d'omplir el cartró evitant nombres repetits
            
            boleta = (random.randint(1, 90))

            if boleta not in cartro:
                cartro.append(boleta)
                num_boletes -= 1
            else: # Aquest else no fa res i es pot treure
                pass
        
        self.cartro = cartro

    def Comprovar(self, boleta):

        if boleta in self.cartro:
            self.cartro.remove(boleta)

        print(f"El cartró del jugador {self.name} queda així:\n{self.cartro}")
