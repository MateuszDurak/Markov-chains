import numpy as np
import matplotlib.pyplot as plt

            # Kamien, Papier, Nozyce
prawd_kamien = [1/3, 1/3, 1/3]  # Kamien
prawd_papier = [1/3, 1/3, 1/3]  # Papier
prawd_nozyce = [1/3, 1/3, 1/3]  # Nozyce
punkty = 0
figury = ['K', 'P', 'N']
prawd_startowe = [1/3, 1/3, 1/3]

def koryguj(prawd, ktora_figura):
    if (ktora_figura == 0):
        prawd[0] = prawd[0] - 0.01
        prawd[1] = prawd[1] + 0.02
        prawd[2] = prawd[2] - 0.01
    elif (ktora_figura == 1):
        prawd[0] = prawd[0] - 0.01
        prawd[1] = prawd[1] - 0.01
        prawd[2] = prawd[2] + 0.02
    else:
        prawd[0] = prawd[0] + 0.02
        prawd[1] = prawd[1] - 0.01
        prawd[2] = prawd[2] - 0.01

def Wynik(gracz, komputer, punkty):
    if ((gracz == 'P' and komputer == 'K')
            or (gracz == 'K' and komputer == 'N')
            or  (gracz == 'N' and komputer == 'P')):
        punkty = punkty + 1
        print('Wygrywasz')
    elif(gracz == komputer):
            print('Remis')
    else:
        punkty = punkty - 1
        print('Przegrywasz')
    return punkty



def gra(ile_gier):
    rundy = np.zeros(int(ile_gier))
    for i in range(int(ile_gier)):
        if int(i) == 0:
            print(f'Gra: {i}')
            poprzedni_ruch = input('Wprowadz K, P lub N: ')
            wybor_komputera = np.random.choice(figury, replace=True, p=prawd_startowe)
            print('Macierz prawdopodobieństwa')
            print('\t\tKamień\t\t\t\tpapier\t\t\t\t\tnożyce')
            print(f'Kamień{prawd_kamien}')
            print(f'Papier{prawd_papier}')
            print(f'Nożyce{prawd_nozyce}')
            print(f'Komputer wybral: {wybor_komputera}')
            rundy[0] = Wynik(poprzedni_ruch, wybor_komputera, punkty)
        else:
            print(f'Gra: {i}')
            aktualny_ruch = input('Wprowadz K, P lub N: ')
            if (poprzedni_ruch == 'K'):
                wybor_komputera = np.random.choice(figury, replace=True, p=prawd_kamien)
                if (aktualny_ruch == figury[0]):
                    koryguj(prawd_kamien, 0)
                if (aktualny_ruch == figury[1]):
                    koryguj(prawd_kamien, 1)
                if (aktualny_ruch == figury[2]):
                    koryguj(prawd_kamien, 2)

            if (poprzedni_ruch == 'P'):
                wybor_komputera = np.random.choice(figury, replace=True, p=prawd_papier)
                if (aktualny_ruch == figury[0]):
                    koryguj(prawd_papier, 0)
                if (aktualny_ruch == figury[1]):
                    koryguj(prawd_papier, 1)
                if (aktualny_ruch == figury[2]):
                    koryguj(prawd_papier, 2)

            if (poprzedni_ruch == 'N'):
                wybor_komputera = np.random.choice(figury, replace=True, p=prawd_nozyce)
                if (aktualny_ruch == figury[0]):
                    koryguj(prawd_nozyce, 0)
                if (aktualny_ruch == figury[1]):
                    koryguj(prawd_nozyce, 1)
                if (aktualny_ruch == figury[2]):
                    koryguj(prawd_nozyce, 2)
            print('Macierz prawdopodobieństwa')
            print('\t\tKamień\t\t\t\tpapier\t\t\t\t\tnożyce')
            print(f'Kamień{prawd_kamien}')
            print(f'Papier{prawd_papier}')
            print(f'Nożyce{prawd_nozyce}')
            print(f'Komputer wybral: {wybor_komputera}')

            rundy[i] = rundy[i-1] + Wynik(aktualny_ruch, wybor_komputera, punkty)

            poprzedni_ruch = aktualny_ruch

    print(f'Historia wyników: {rundy}')
    plt.plot(rundy, 'ro')
    plt.show()
def main():
    ile_gier = input('ile iteracji?: ')
    gra(ile_gier)

if __name__ == '__main__':
    main()