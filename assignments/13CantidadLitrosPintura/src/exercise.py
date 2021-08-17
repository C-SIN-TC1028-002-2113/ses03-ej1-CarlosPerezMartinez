def main():
    #escribe tu código abajo de esta línea
    import math
    AreaAPintar=float(input('Area a pintar en metros: '))
    Rendimiento=float(input('Rendimiento (m2/l): '))
    LitrosAComprar=AreaAPintar/Rendimiento
    print('Litros a comprar:',math.ceil(LitrosAComprar))

if __name__ == '__main__':
    main()
