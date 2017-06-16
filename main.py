#crear lista de imagenes y guardarlas
class Listaimagen:
	def __init__(self):
		self.lista=[]
#crear una biblioteca con varias carpetas
#utilizo el .txt pero no se si este ya bien emplementado el codigo 
	def almacenar(self):
		try
		os.mkdir(os.path.dirname(os.path.realpath(__file__))+'/etiquetada')
		except:
			pass
		 guardado=os.path.dirname(os.path.realpath(__file__))+'/etiquetada'
		 informacion=open(guardado+'/'+'informacion.txt','a')
		if os.path.exists(carpeta)==True:
			if os.path.isdir(carpeta)==True:
		for archivo in os.listdir(carpeta):
			if os.path.isfile(carpeta+'/'+archivo)==True:
				if archivo.lower().endswith((('.png', '.jpg', '.gif')):
					ver=Image.open(carpeta+'/'+archivo)
					ver.show()
					etiqueta=raw_input('Etiqueta ')
					shutil.copy2(carpeta+'/'+archivo,guardado)
					self.lista.append(Etiqueta(guardado+'/'+archivo,etiqueta))
					informacion.write(archivo+' '+etiqueta+' '+'\n')
					else:
						pass
					elif os.path.isdir(carpeta+'/'+archivo)==True:
						self.almacenar(carpeta+'/'+archivo)
					else:
						pass
			else:
				print 'ruta dada no existe'
		else:
			print 'la carpeta no existe'
		informacion.close()
#Aqui cuenta las etiquetas como su nombre lo dice	
	def contar_etiquetas(self):
		etiquetas={}
		for i in self.lista:
			if i.etiqueta in etiquetas:
				etiquetas[i.etiqueta]+=1
			else:
				etiquetas[i.etiqueta]=1
		return etiquetas

		
#REvisa las imagenes guardadas en la lista
	def revisar(self):
		if os.path.isdir(os.path.dirname(os.path.realpath(__file__))+'/etiqueta')==True:
			if os.path.isfile(os.path.dirname(os.path.realpath(__file__))+'/etiquetada/informacion.txt'):
				informacion=open(os.path.dirname(os.path.realpath(__file__))+'/etiquetada/informacion.txt','r')
				for linea in informacion:
					archivo,etiqueta,comentario=linea.split()
					if os.path.isfile(os.path.dirname(os.path.realpath(__file__))+'/etiquetada/'+archivo):
						self.lista.append(Etiqueta(os.path.dirname(os.path.realpath(__file__))+'/etiquetado/'+archivo,etiqueta,comentario))
					else:
						pass
			else:
				print 'falta archivo de informacion'
		else:
			pass
	
