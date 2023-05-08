# Mensaje de bienvenida
print("\033[1m"+"\nBienvenid@ al programa."+"\033[0m")

# datos que se usaran en el programna.

def funcion():
    # Array con los departamentos del pais.
    departamentos = ["Chalatenango","San Salvador","Santa Ana","Cuscatlan","La Paz","La Libertad","Morazán","Sonsonate","San Miguel","San Vicente","La Unión","Cabañas","Ahuachapan","Usulutan"]

    # Arrays de cada departamento del pais que almecenen sus municipios.
    chalatenango = ["Agua Caliente.","Arcatao.","Azacualpa.","Chalatenango.","Citalá.","Comalapa.","Concepción Quezaltepeque.","Dulce Nombre de María.","El Carrizal.","El Paraiso.","La Laguna.","La Palma.","La Reina.","Las Vueltas.","Nombre de Jesús.","Nueva Concepción.","Nueva Trinidad.","Ojos de agua.","Potonico.","San Antonio de la Cruz.","San Antonio Los Ranchos.","San Fernando.","San Francisco Lempa.","San Francisco Morazán.","San Ignacio.","San Isidro Labrador.","San José Cancasque.","San José Las Flores.","San Luis del Carmen.","San Miguel de Mercedes.","San Rafael.","Santa Rita.","Tejutla."]
    sanSalvador = ["Aguilares.","Apopa","Ayutuxtepeque.","Cuscatancingo.","Ciudad Delgado.","El Paisnal.","Guazapa.","Ilopango.","Mejicanos.","Nejapa.","Panchimalco.","Rosario de Mora.","San Marcos.","San Martín.","San Salvador.","Santiago Texacuangos.","Santo Tomás.","Soyapango.","Tonacatepeque"]
    santaAna = ["Candelaria de La frontera","Chalchuapa","Coatepeque","El congo","El Porvenir","Masahuat","Metapan","San Antonio Pajonal","San Sebastian Saltrillo","Santa Ana","Santa Rosa Guachiplin","Santiago de la frontera","Texistepeque"]
    cuscatlan = ["Candelari","Cojutepeque","El Carmen","El Rosario","Monte San Juan","Oratorio de Concepción","San Bartolomé Perulapía","San Cristóbal","San José Guayabal","San Pedro Perulapán","San Rafael Cedros","San Ramón","Santa Cruz Analquito","Santa Cruz Michapa","Suchitoto","Tenancingo"]
    laPaz = ["Zacatecoluca","Cuyultitán","El Rosario","Jerusalén","Mercedes La Ceiba","Olocuilta","Paraíso de Osorio","San Antonio Masahuat","San Emigdio","San Francisco Chinameca","San Pedro Masahuat","San Juan Nonualco","San Juan Talpa","San Juan Tepezontes","San Luis La Herradura","San Luis Talpa","San Miguel Tepezontes","San Pedro Nonualco","San Rafael Obrajuelo","Santa María Ostuma","Santiago Nonualco","Tapalhuaca"]
    SanMiguel = ["Chapeltique", "Chinameca", "Chirilagua", "Ciudad Barrios", "Comacarán", "El Tránsito", "Lolotique", "Moncagua", "Nueva Guadalupe", "Nuevo Edén de San Juan", "Quelepa", "San Antonio", "San Gerardo", "San Jorge", "San Luis de la Reina"]
    LaLibertad = ["Antiguo Cuscatlán", "Chiltiupán", "Ciudad Arce", "Colón" "Comasagua", "Huizúcar", "Jayaque", "Jicalapa", "La Libertad", "Santa Tecla", "Nuevo Cuscatlán", "San Juan Opico", "Quezaltepeque", "Sacacoyo", "San José Villanueva", "San Matías", "San Pablo Tacachico", "Talnique", "Tamanique", "Teotepeque", "Tepecoyo", "Zaragoza"]
    Morazán = ["Arambala", "Cacaopera", "Chilanga", "Corinto", "Delicias de Concepción", "El Divisadero", "El Rosario", "Gualococti", "Guatajiagua", "Joateca", "Jocoaitique", "Jocoro", "Lolotiquillo", "Meanguera", "Osical", "Perquín", "San Carlos", "San Fernando", "San Francisco Gotera", "San Isidro", "San Simón", "Sensembra", "Sociedad", "Torola", "Yamabal", "Yoloaiquín"]
    sonsonate = ["Acajutla", "Armenia", "Caluco", "Cuisnahuat", "Izalco", "Juayúa", "Nahuizalco", "Nahulingo", "Salcoatitán", "San Antonio del Monte", "San Julián", "Santa Catarina Masahuat", "Santa Isabel Ishuatán", "Santo Domingo de Guzmán", "Sonsonate", "Sonzacate"]
    sanVicente = ["Apastepeque", "Guadalupe", "San Cayetano Istepeque", "San Esteban Catarina", "San Ildefonso", "San Lorenzo", "San Sebastián", "San Vicente", "Santa Clara", "Santo Domingo", "Tecoluca", "Tepetitán", "Verapaz"]
    laUnion = ["Anamorós", "Bolívar", "Concepción de Oriente", "Conchagua", "El Carmen", "El Sauce", "Intipucá", "La Unión", "Lislique", "Meanguera del Golfo", "Nueva Esparta", "Pasaquina", "Polorós", "San Alejo", "San José", "Santa Rosa de Lima", "Yayantique", "Yucuaiquín"]
    cabañas = ["Cinquera"," Dolores","Guacotecti","Ilobasco", "Jutiapa", "San Isidro ","Sensuntepeque", "Tejutepeque", "Victoria"]
    ahuachapan = ["Ahuachapán", "Apaneca"," Atiquizaya", "Concepción de Ataco", "El Refugio", "Guaymango", "Jujutla", "San Francisco Menéndez", "San Lorenzo ", " San Pedro", "Puxtla", "Tacuba", "Turín"]
    usulutan = ["Alegría", "Berlín", "California", "Concepción Batres", "El Triunfo", "Ereguayquín", "Estanzuelas", "Jiquilisco", "Jucuapa", "Jucuarán", "Mercedes Umaña", "Nueva Granada", "Ozatlán", "Puerto El Triunfo", "San Agustín", "San Buenaventura", "San Dionisio", "San Francisco Javier", "Santa Elena", "Santa María", "Santiago de María", "Tecapán", "Usulután" ]
    

    while True:
        print("\033[1m"+"\nMenú\n"+"\033[0m")

        for i in departamentos:
            print(i)

        dep = input("\nSeleccione un departamento del menu anterior -> ").lower()
        print("--------------------------------------------------------------")
        cont = 0
        
        # condicion que marque a cada departamento.
        if dep == "chalatenango":
            print("\nLos municipios del departamento de chalatenango son:\n")
            for i in chalatenango:
                cont += 1
                print(f"{cont}. {i}")
            break

        elif dep == "san salvador":
            print("\nLos municipios del departamento de San Salvador son:\n")
            for i in sanSalvador:
                cont += 1
                print(f"{cont}. {i}")
            break
         
        elif dep == "santa ana":
            print("\nLos municipios del departamento de Santa Ana son:\n")
            for i in santaAna:
                cont += 1
                print(f"{cont}. {i}")
            break
        
        elif dep == "cuscatlan":
            print("\nLos municipios del departamento de Cuscatlan son:\n")
            for i in cuscatlan:
                cont += 1
                print(f"{cont}. {i}")
            break
                
        elif dep == "la paz":
            print("\nLos municipios del departamento de La Paz son:\n")
            for i in laPaz:
                cont += 1
                print(f"{cont}. {i}")
            break

        elif dep == "san miguel":
            print("\nLos municipios del departamento de Cuscatlan son:\n")
            for i in SanMiguel:
                cont += 1
                print(f"{cont}. {i}")
            break
                
        elif dep == "la libertad":
            print("\nLos municipios del departamento de La Paz son:\n")
            for i in LaLibertad:
                cont += 1
                print(f"{cont}. {i}")
            break

        elif dep == "morazán":
            print("\nLos municipios del departamento de La Paz son:\n")
            for i in Morazán:
                cont += 1
                print(f"{cont}. {i}")
            break
                
        elif dep == "sonsonate":
            print("\nLos municipios del departamento de Sonsonate son:\n")
            for i in sonsonate:
                cont += 1
                print(f"{cont}. {i}")
            break
                
        elif dep == "san vicente":
            print("\nLos municipios del departamento de San Vicente son:\n")
            for i in sanVicente:
                cont += 1
                print(f"{cont}. {i}")
            break
                
        elif dep == "la union":
            print("\nLos municipios del departamento de La Unión son:\n")
            for i in laUnion:
                cont += 1
                print(f"{cont}. {i}")
            break

        elif dep == "usulutan":
            print("\nLos municipios del departamento de Usulutan son:\n")
            for i in usulutan:
                cont += 1
                print(f"{cont}. {i}")
            break
        
        elif dep == "cabañas":
            print("\nLos municipios del departamento de Cabañas son:\n")
            for i in cabañas:
                cont += 1
                print(f"{cont}. {i}")
            break
        
        elif dep == "ahuachapan":
            print("\nLos municipios del departamento de Ahuachapan son:\n")
            for i in ahuachapan:
                cont += 1
                print(f"{cont}. {i}")
            break
        else:
            print("Por favor asegurese de escribir corectamente el departamento")
   
pregunta = input("\n¿Desea ejecutar el programa? \nSI    o    No  --->").lower()
while True:
    if pregunta == "si":
        print("--------------------------------------------------------------")
        funcion()
        print("--------------------------------------------------------------")
        pregunta = input("Desea consultar otro departamento \nSi   o   No  --->")
    elif pregunta == "no":
        print("--------------------------------------------------------------")
        print("\nEntendido, el programa se cerrara")
        break
    else:
        print("--------------------------------------------------------------")
        pregunta = input("\nIngrese una de las repuestas solicitadas \nSi   o   No --->").lower()

print("\nFin del programa.\n")