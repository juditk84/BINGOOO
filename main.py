import random
from Jugador import jugador

# fem un bingo, amo ayá

BOLETES_LIST = []

def TreureBoleta(): # treiem boleta i mirem si ja ha sortit o no:

    boleta_valida = True

    while boleta_valida: # no em sembla la forma més inteligible de fer-ho però yo què sé

        boleta = random.randint(1, 90)

        if boleta not in BOLETES_LIST:
            BOLETES_LIST.append(boleta)
            break

        else:
            pass
        
    print(f"ha sortit el número {boleta}")
    # Comprovar(boleta)
    
    return boleta

# em faig instàncies de jugadors:
Jugador_1 = jugador("Bonico del tó")
Jugador_2 = jugador("Ratzinger")

# les fico en una llista per poder iterar amb loops, because why not:
JUGADORS = [Jugador_1, Jugador_2]

final_joc = None

# inicialitzo els cartrons de cada jugador:
for player in JUGADORS:
    player.OmplirCartro()
    print(f"el cartró del jugador {player.name} té els següents números:\n{player.cartro}\n")

while final_joc != "BINGO!": # grans temptacions de fer while True i sortir quan toqui amb break,
                             # però entenc que és més readable amb variables?
     
    input("apreta qualsevol tecla per treure una altra boleta ^^\n") # m'ho poso així per tenir una mínima pausa jiji
    
    new_boleta = TreureBoleta() # CREC que així ta guai, però no sé

    for player in JUGADORS:

        player.Comprovar(new_boleta)

        if player.cartro: # oséase, si la llista té contingut...
            pass
        else: # si la llista és false, meaning it's empty...
            print(f"el jugador {player.name} ha fet BINGO!")
            final_joc = "BINGO!"

# al principi havia fet la funció Comprovar() fora de la classe Jugador, però
# tot i que funcionava, crec que té més sentit així. Però no sé