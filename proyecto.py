import matplotlib.pyplot as plt
import matplotlib.image as im
import glob
import numpy

class clasificador(object):
    '''
        Esta clase clasifica todos los animales supervisada por el usuario
    '''
    def leer_imagenes(self):

        #creamos una lista para almacenar todas la imagenes
        todas_imagenes = []

        #hacemos un ciclo para leer todos las imagenes de dicho directorio
        #   glob se encarga de leer todas las extensionde con .png
        for filename in glob.glob('*.png'):

            #leemos la imagen
            img = im.imread(filename)

            #las agregamos a la lista para despues pricesarlas
            todas_imagenes.append(img)

        return todas_imagenes

    def clasificar(self):

        todas_imagenes = self.leer_imagenes()
        for actual_imagen in todas_imagenes:
            plt.imshow(actual_imagen);
	    plt.show()

            categoria = raw_input('A que categoria pertenece este animal\n')
            etiqueta = raw_input('Escribe el nombre del animal\n')

            im.imsave('animales/'+str(categoria)+'_'+str(etiqueta)+'.png',actual_imagen)
            
		 
    def buscar(self):
	todas_imagenes = []
	bus = raw_input('Palabra clave: ')
	for filename in glob.glob('animales/*.png'):
	    if bus in filename:
               img = im.imread(filename)
	       todas_imagenes.append(img)
	    for actual in todas_imagenes:
		plt.imshow(actual)
		plt.show
	    
#llamamos a la clase que se encarga de clasificar todas la imagenes
clasificador().clasificar()
op = raw_input('Buscar imagen (S/n): ')
if op=='S' or op =='s':
	clasificador().buscar()
