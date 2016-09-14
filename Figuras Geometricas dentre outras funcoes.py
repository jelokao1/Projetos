#Autor: Félix Licht and Samuel Araujo
#Inicio do projeto: 10/09/2016
#Tema: Calcular Perimetro e areas de fuguras geometricas
#Calcular equações de segundo grau
#Dentre outras ferramentas que serão implatadas
#python 3.5

import math

    #Perimetro
#Soma dos lados da figura

#Area
#Multiplicacao da haltura e base

print ("Deseja descobrir o PERIMETRO ou AREA das figuras geometricas? ")
ope = input (" 01 - Perimetro \n 02 - Area \n 03 - Equacao de segundo grau \n")

#Perimetro
if(ope == '01' or ope == '1'):
    print("PERIMETRO ")
    print("De qual figura geometrica deseja achar o perimetro? ")
    print ("01 - Quadrado \n02 - Retangulo \n03 - Triangulo \n04 - Losango \n05 - Paralelograma \n06 - Trapezio \n07 - Circunferencia \n")

    figu = input ("Digite o numero da figura desejada: ")
    #Quadrado
    if (figu == '01' or figu == '1'):
        print("PERIMETRO ")
        print("\n QUADRADO")
        lado = float(input("Informe o lado do quadrado: "))
        perimetro = 4 *lado
        print("\nQual a forma de medida ")
        medida = input("M - Metros \nC - Centimentros ")
        if(medida == 'M' or medida == 'm'):
            print ("\nO perimetro e = %.2f Metros " %perimetro)
        elif (medida == 'C' or medida == 'c'):
            cm = perimetro/100
            print("\nO perimetro e = %.2f Centimetro " %cm)
    #Retangulo
    elif(figu == '02' or figu == '2'):
        print("PERIMETRO ")
        print("\nRETANGULO")
        base = float(input("Informe a base do retangulo: "))
        haltura =float(input("Informe a haltura do retangulo: "))
        perimetro = (base*2) + (haltura*2)
        print("\nQual a forma de medida ")
        medida = input("M - Metros \nC - Centimentros ")
        if(medida == 'M' or medida == 'm'):
            print ("\nO perimetro e = %.2f Metros " %perimetro)
        elif (medida == 'C' or medida == 'c'):
            cm = perimetro/100
            print("\nO perimetro e = %.2f Centimetro " %cm)
    #Triangulo
        #Planejando ainda
            # um triangulo tem que ter-  l1 <l2 + l3 e l2 < l3 + l1
    elif (figu == '03' or figu == '3'):
        print("PERIMETRO ")
        print("TRIANGULO ")
        print("Informe os tres lados do Triangulo: ")
        lado1 = float(input("Informe o Lado 1 "))
        lado2 = float(input("Informe o Lado 2 "))
        lado3 = float(input("Informe o Lado 3 "))
        if(lado1 < lado2 + lado3 and lado2 < lado3 + lado1):
            if(lado1 == lado2 and lado2 == lado3):
                print("Forma um Triangulo EQUILATERO: ")
                perimetro = (lado1 + lado2 + lado3)
                print("\nQual a forma de medida ")
                medida = input("M - Metros \nC - Centimentros ")
                if(medida == 'M' or medida == 'm'):
                     print ("\nO perimetro e = %.2f Metros " %perimetro)
                elif (medida == 'C' or medida == 'c'):
                     cm = perimetro/100
                     print("\nO perimetro e = %.2f Centimetro " %cm)
                
            elif(lado1 == lado2 or lado1 == lado3 or lado3 == lado2):
                print ("Triangulo ISOICELES ")
                perimetro = (lado1 + lado2 + lado3)
                print("\nQual a forma de medida ")
                medida = input("M - Metros \nC - Centimentros ")
                if(medida == 'M' or medida == 'm'):
                     print ("\nO perimetro e = %.2f Metros " %perimetro)
                elif (medida == 'C' or medida == 'c'):
                     cm = perimetro/100
                     print("\nO perimetro e = %.2f Centimetro " %cm)

            else:
                print("ESCALENO ")
                perimetro = (lado1 + lado2 + lado3)
                print("\nQual a forma de medida ")
                medida = input("M - Metros \nC - Centimentros ")
                if(medida == 'M' or medida == 'm'):
                     print ("\nO perimetro e = %.2f Metros " %perimetro)
                elif (medida == 'C' or medida == 'c'):
                     cm = perimetro/100
                     print("\nO perimetro e = %.2f Centimetro " %cm)

        else:             
          print("Os valors nao formam um triangulo ")
          print ("\n AS regras para que um triangulo seja formada sao: ")
          print ("\n 01 - O lado 1 deve ser menor que a soma dos Lados 2 e 3")
          print (" 02 - O lado 2 deve ser menor que a soma dos Lados 1 e 3")
          print (" 03 - O lado 3 deve ser menor que a soma dos Lados 2 e 1")
       



    #Losango
    elif (figu == '04' or figu == '4'):
          print("PERIMETRO ")
          print("\n LOSANGO")
          lado = float(input("Informe o lado do losango: "))
          perimetro = 4 *lado
          print("\nQual a forma de medida ")
          medida = input("M - Metros \nC - Centimentros ")
          if(medida == 'M' or medida == 'm'):
             print ("\nO perimetro e = %.2f Metros " %perimetro)
          elif (medida == 'C' or medida == 'c'):
             cm = perimetro/100
             print("\nO perimetro e = %.2f Centimetro " %cm)
    #Paralelograma
    elif (figu == '05' or figu == '5'):
          print("PERIMETRO ")
          print("\n PARALELOGRAMA")
          base = float(input("Informe a base do paralelograma: "))
          haltura = float(input("Informe a haltura do paralelograma: "))
          perimetro = 2 * ( base * haltura )
          print("\nQual a forma de medida ")
          medida = input("M - Metros \nC - Centimentros ")
          if(medida == 'M' or medida == 'm'):
             print ("\nO perimetro e = %.2f Metros " %perimetro)
          elif (medida == 'C' or medida == 'c'):
             cm = perimetro/100
             print("\nO perimetro e = %.2f Centimetro " %cm)

    #Trapezio   
    elif (figu == '06' or figu == '6'):
          print("PERIMETRO ")
          print("\n TRAPEZIO")
          basemenor = float(input("Informe a BASE MENOR do trapezio: "))
          basemaior = float(input("Informe a BASE MAIOR do trapezio: "))
          v1 = float(input("Informe o VRTICE 1 do trapezio: "))
          v2 = float(input("Informe o VERTICE 2 do trapezio: "))
          if(basemenor == basemaior or v1 == v2):
              print("\nNao forma um TRAPEZIO ")
          elif(basemenor != basemaior and v1 != v2):
              perimetro = basemenor+basemaior+v1+v2
              print("\nQual a forma de medida ")
              medida = input("M - Metros \nC - Centimentros ")
              if(medida == 'M' or medida == 'm'):
                 print ("\nO perimetro e = %.2f Metros " %perimetro)
              elif (medida == 'C' or medida == 'c'):
                 cm = perimetro/100
                 print("\nO perimetro e = %.2f Centimetro " %cm)

    #Circunferencia
    elif (figu == '07' or figu == '7'):
          print("PERIMETRO ")
          print("\n CIRCUNFERENCIA")
          print("Voce sabe o raio ou diametro? ")
          informacao = input("01 - Raio \n02 - Diametro ")
          if (informacao == '01' or informacao == '1'):
              raio = float (input("\nInforme o raio: "))
              pi = 3.14
              perimetro = 2 * (pi * raio)
              print("\nQual a forma de medida ")
              medida = input("M - Metros \nC - Centimentros ")
              if(medida == 'M' or medida == 'm'):
                 print ("\nO perimetro e = %.2f Metros " %perimetro)
              elif (medida == 'C' or medida == 'c'):
                 cm = perimetro/100
                 print("\nO perimetro e = %.2f Centimetro " %cm)

          elif (informacao == '02' or informacao == '2'):
                diametro = float(input("Informe o diametro: "))
                raio = (diametro /2)
                pi = 3.14
                perimetro = 2 * (pi * raio)
                print("\nQual a forma de medida ")
                medida = input("M - Metros \nC - Centimentros ")
                if(medida == 'M' or medida == 'm'):
                    print ("\nO perimetro e = %.2f Metros " %perimetro)
                elif (medida == 'C' or medida == 'c'):
                    cm = perimetro/100
                    print("\nO perimetro e = %.2f Centimetro " %cm)     
           


                                                               
#Area    
elif (ope == '02' or ope == '2'):
    print("AREA ")
    print ("\n01 - Quadrado \n02 - Retangulo \n03 - Triangulo \n04 - Losango \n05 - Paralelograma \n06 - Trapezio \n07 - Circunferencia \n")
    print("De qual figura geometrica deseja achar o perimetro? ")
    figu = input ("Digite o numero da figura desejada: ")
    
    #Quadrado
    if(figu == '01' or figu == '1'):
        print("AREA ")
        print ("QUADRADO ")
        lado = float(input("Informe o lado do quadrado"))
        area = 4 * lado
        print("\nQual a forma de medida ")
        medida = input("M - Metros \nC - Centimentros ")
        if(medida == 'M' or medida == 'm'):
           print ("\nA area e = %.2f Metros² " %area)
        elif (medida == 'C' or medida == 'c'):
           print("\nA area e = %.2f Centimetro²" %area)
    
    #Retangulo
    elif (figu == '02' or figu == '2'):
        print("AREA ")
        print ("RETANGULO ")
        lado1 = float(input("Informe o lado do retangulo "))
        base = float(input("Informe a base do retangulo "))
        area = (base*base) + (lado1*lado1)
        print("\nQual a forma de medida ")
        medida = input("M - Metros \nC - Centimentros ")
        if(medida == 'M' or medida == 'm'):
             print ("\nO perimetro e = %.2f Metros² " %area)
        elif (medida == 'C' or medida == 'c'):
            print("\nO perimetro e = %.2f Centimetro²" %area)
            
    #Triagulo
    elif (figu == '03' or figu == '3'):
        print("AREA ")
        print("TRIANGULO ")
        print("Informe os tres lados do Triangulo: ")
        lado1 = float(input("Informe o Lado 1 "))
        lado2 = float(input("Informe o Lado 2 "))
        lado3 = float(input("Informe o Lado 3 "))
        if(lado1 < lado2 + lado3 and lado2 < lado3 + lado1):
            if(lado1 == lado2 and lado2 == lado3):
                print("Forma um Triangulo EQUILATERO: ")
                perimetro = (lado1 + lado2 + lado3)
                print("\nQual a forma de medida ")
                medida = input("M - Metros \nC - Centimentros ")
                if(medida == 'M' or medida == 'm'):
                     print ("\nA Area e = %.2f Metros " %perimetro)
                elif (medida == 'C' or medida == 'c'):
                     cm = perimetro/100
                     print("\nA Area e = %.2f Centimetro " %cm)
                
            elif(lado1 == lado2 or lado1 == lado3 or lado3 == lado2):
                print ("Triangulo ISOICELES ")
                perimetro = (lado1 + lado2 + lado3)
                print("\nQual a forma de medida ")
                medida = input("M - Metros \nC - Centimentros ")
                if(medida == 'M' or medida == 'm'):
                     print ("\nA Area e = %.2f Metros " %perimetro)
                elif (medida == 'C' or medida == 'c'):
                     cm = perimetro/100
                     print("\nA Area e = %.2f Centimetro " %cm)

            else:
                print("ESCALENO ")
                perimetro = (lado1 + lado2 + lado3)
                print("\nQual a forma de medida ")
                medida = input("M - Metros \nC - Centimentros ")
                if(medida == 'M' or medida == 'm'):
                     print ("\nA Area e = %.2f Metros " %perimetro)
                elif (medida == 'C' or medida == 'c'):
                     cm = perimetro/100
                     print("\nA Area e = %.2f Centimetro " %cm)

        else:             
          print("Os valors nao formam um triangulo ")
          print ("\n AS regras para que um triangulo seja formada sao: ")
          print ("\n 01 - O lado 1 deve ser menor que a soma dos Lados 2 e 3")
          print (" 02 - O lado 2 deve ser menor que a soma dos Lados 1 e 3")
          print (" 03 - O lado 3 deve ser menor que a soma dos Lados 2 e 1")
       

            
    #Losango
    elif (figu == '04' or figu == '4'):
        print("AREA ")
        print ("LOSANGO ")
        dmenor = float(input("Informe a Diagonal Menor do Losango "))
        dmaior = float(input("Informe a Diagonal Maior  do Losango "))
        area = (dmaior * dmenor) /2
        if(dmaior <= dmenor ):
            print("\n Diagonal maior nao poder ser menor que a Diagonal menor.")
        elif(dmaior > dmenor):
            print("\nQual a forma de medida ")
            medida = input("M - Metros \nC - Centimentros ")
            if(medida == 'M' or medida == 'm'):
                print ("\nA area e = %.2f Metros² " %area)
            elif (medida == 'C' or medida == 'c'):
                print("\nA area e = %.2f Centimetro²" %area)
                
    #Paralelograma
    elif (figu == '05' or figu == '5'):
        print("AREA ")
        print ("PARALELOGRAMA ")
        haltura = float(input("Informe a haltura do Paralelograma "))
        base = float(input("Informe a base do Paralelograma  "))
        area = (base*haltura) 
        print("\nQual a forma de medida ")
        medida = input("M - Metros \nC - Centimentros ")
        if(medida == 'M' or medida == 'm'):
           print ("\nA area e = %.2f Metros² " %area)
        elif (medida == 'C' or medida == 'c'):
           print("\nA area e = %.2f Centimetro²" %area)
           
    #Trapezio
    elif (figu == '06' or figu == '6'):
        print("AREA ")
        print("TRAPEZIO ")
        basemaior = float(input("Informe a Maior Base do Paralelograma "))
        basemenor = float(input("Informe a Menor Base do Paralelograma  "))
        haltura = float(input("Informe a Haltura do Paralelograma "))
        area = ((basemaior*basemenor)*2)/2 
        print("\nQual a forma de medida ")
        medida = input("M - Metros \nC - Centimentros ")
        if(medida == 'M' or medida == 'm'):
           print ("\nA area e = %.2f Metros² " %area)
        elif (medida == 'C' or medida == 'c'):
           print("\nA area e = %.2f Centimetro²" %area)
        
    #Circunferencia
           #Raio
    elif (figu == '07' or figu == '7'):
        print("AREA ")
        print("CIRCUNFERENCIA ")
        print("Voce sabe o raio ou diametro? ")
        informacao = input("01 - Raio \n02 - Diametro ")
        if (informacao == '01' or informacao == '1'):
            raio = float (input("\nInforme o raio: "))
            pi = 3.14
            area = 2 * (pi * raio)
            print("\nQual a forma de medida ")
            medida = input("M - Metros \nC - Centimentros ")
            if(medida == 'M' or medida == 'm'):
                print ("\nA Area e = %.2f Metros " %area)
            elif (medida == 'C' or medida == 'c'):
                print("\nA Area e = %.2f Centimetro " %area)

            #Diametro
        elif (informacao == '02' or informacao == '2'):
              diametro = float(input("Informe o diametro: "))
              raio = (diametro /2)
              pi = 3.14
              area = 2 * (pi * raio)
              print("\nQual a forma de medida ")
              medida = input("M - Metros \nC - Centimentros ")
              if(medida == 'M' or medida == 'm'):
                 print ("\nA Area e = %.2f Metros " %area)
              elif (medida == 'C' or medida == 'c'):
                 print("\nA Area e = %.2f Centimetro " %area)   

#Equação de Segundo Grau
elif (ope == '03' or ope == '3'):
    print("EQUACAO DE SEGUNDO GRAU ")
    a = int(input("Informe A "))
    b = int(input("Informe B "))
    c = int(input("Informe C "))
    print("\nA equacao fica: ")
    print(a,"x²+",b,"x+",c,"= 0")

    #Delta = b²-4ac
    delta = (b**2) - 4*a*c
    print("\n Delta vale = %1.0f" %delta)
    if(delta < 0):
        print("\nDELTA NÃO PODE SER MENOR QUE '0' ")
    else:
        x1 = ((-1 * b) + (math.sqrt (delta)))/(2*a)
        print ("x¹ vale %2.2f " %x1)
        x2 = ((-1 * b) - (math.sqrt (delta)))/(2*a)
        print("x² vale %2.2f " %x2)

