## Hola Otty sigo pendiente de estos cambios que aparecen en este archivo
## avisame en cuanto actualizes este archivo

Ruta = "otty"
ListaImagenes = []
Para cada carpeta en Ruta hacer:
  ListaDirectorios <=LeerDirectorio
  si hay imagenes
    para cada imagen hacer:
        nuvImagen = Imagen("nombre",Ruta,"")
        ListaImagenes.append(nuvImagen)
  continuar a la siguiente carpeta
 
 clasificador(listaImagenes)
