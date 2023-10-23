from django.shortcuts import render

# Create your views here.


def app2(request):
    return render(request, 'appLibros/libros.html')

def mistborn(request):
    data={
        "titulo":"Nacidos de la Bruma",
        "imagen":"imagenes/cosmere_symbol.png",
        "imagenlibro":"imagenes/mistborn.jpg",
        "dato1":"Actualmente se han escrito 7 libros de la serie Nacidos de La Bruma, se cree que toda la saga abarcara de entre 13 a 16 libros",
        "dato2":"Se divide en 4 eras, la primera Era conformada por tres libros: El Imperio Final, El Pozo de la Ascencion y El Heroe de las Eras, su ambientacion es parecida a la epoca medieval humana. La segunda era conformada por cuatro libros: Aleacion de Ley, Sombras de Identidad, Brazales de Duelo y El Metal Perdido, donde la ambientacion es parecida a los inicios de la era industrial humana. La tercera era aun no ha sido escrita pero se desarrollara en una epoca parecida a las años 80 y el inicio de la guerra fria. La cuarta era aun no ha sido escrita pero se desarrollara en los inicio de los viajes interestelares",
        "dato3":"Nacidos de la Bruma tiene lugar en el planeta Scadrial un analogo de la tierra, un planeta donde los habitantes pueden nacer con ciertos poderes, la Alomancia y la Feruquimia, ambas relacionadas al uso de 16 metales, ademas existe una tercera manera de portar aquellos poderes, mediante la Hemalurgia donde se asesinan a portadores de estos poderes y son robados mediante clavos hemalurgicos",
        "dato4":"Parte del Cosmere, el universo fictio de BRANDON SANDERSON, que gradualmente avanzara de la fantasia epica a la ciencia ficcion",
    }
    return render(request, 'appLibros/libros.html', data)

def stormlight(request):
    data={
        "titulo":"El Archivo de Las Tormentas",
        "imagen":"imagenes/cosmere_symbol.png",
        "imagenlibro":"imagenes/shallan.jpg",
        "dato1":"Actualmente se han escrito 4 libros de la decalogia del Archivo de las Tormentas, ademas de dos novelas complementarias",
        "dato2":"Se divide en dos principales arcos argumentales, el primero terminando dentro de un año con el quinto libro (Saldra a finales de noviembre del 2024), contiene personajes muy humanos, con sus problemas, temores y cargas y muestra sus evoluciones a lo largo de los libros",
        "dato3":"El Archivo de Las Tormentas tiene lugar en el planeta Roshar, Con la excepción de Shinovar y algún lait bien protegido, todo Roshar es frecuentemente asolado por altas tormentas, enormes huracanes que viajan de este a oeste. Dentro del planeta existen diez poderes (Potencias) y cada humano es capaz de ocupar dos de estas al pertenecer a una de las ya disueltas Ordenes de Caballeros Radiantes",
        "dato4":"Parte del Cosmere, el universo fictio de BRANDON SANDERSON, que gradualmente avanzara de la fantasia epica a la ciencia ficcion",
    }
    return render(request, 'appLibros/libros.html', data)

def sunlit(request):
    data={
        "titulo":"El Hombre Iluminado",
        "imagen":"imagenes/cosmere_symbol.png",
        "imagenlibro":"imagenes/elegy.jpg",
        "dato1":"Unico libro de una 500 paginas aprox, relacionado intimamente con el Archivo de las Tormentas",
        "dato2":"Se recomienda encarecidamente leer tras el cuarto libro del Archivo de las Tormentas",
        "dato3":"El Hombre Iluminado tiene lugar en Cantico, un planeta enano asolado por un poderoso dia que barre con todo la organico e inorganico debido a las altas temperaturas que irradia, su poblacion escapa constantemente de este terrible destino en ciudades-nave alimentadas por Soles Corazon",
        "dato4":"Parte del Cosmere, el universo fictio de BRANDON SANDERSON, que gradualmente avanzara de la fantasia epica a la ciencia ficcion",
    }
    return render(request, 'appLibros/libros.html', data)
