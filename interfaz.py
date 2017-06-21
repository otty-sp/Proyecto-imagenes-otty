import os
from Tkinter import *
from PIL import Image


def tag(numID,tag,ob_img):
  for i in ob_img:
  if i.num == numID:
  i.tags.append(tag)
#Funcion que abre en el formato gif a una imagen
/* Esta funcion requiere que le pases el num de imagen */
def abrir_img(path_img):
    path_temp = path_img +".gif"
  try:
    Image.open(path_img).save(path_temp)
    except IOError:
    print("No se puede convertir la imagen")
    imagen1 = PhotoImage(file=path_temp)
  return imagen1
  

## Utiliza esta idea

def getImg(self, img):
        self.masterImg = Image.open(os.path.join("images",
                                  self.images[img]))
        self.masterImg.thumbnail((400, 400))
        self.img = ImageTk.PhotoImage(self.masterImg)
        self.lbl['image'] = self.img


  
def mostrar_interfaz(ob_img):
  num = buscar_avance(ob_img) 

  ventana = Tk()
  ventana.title("Clasificador de Imagenes")
  ventana.config(bg="gray")
  ventana.geometry("600x700")
  Label = Label(ventana, image = abrir_img(ob_img[0].ruta))
  Label.grid(row=1,column=2)
  boton1 = button(ventana,"siguiente")
  boton1.button.grid(row=1,column=1)
  boton2 = button(ventana, "anterior")
  boton2.button.grid(row=1,column=2)
  boton3 = button(ventana, "finalizar")
  boton3.button.grid(row=1,column=3)
  ventana.mainloop()

ob_img = []
path_carpeta = raw_input("introduce la direcion de la carpeta que contiene las imagenes")
path_carpetas = comprobar_carpeta(path_carpeta)
print path_carpetas
for i in path_carpetas:
nom_img_temp = nom_files(i)
ob_img_temp = crear_ob_img(nom_img_temp,i)
for j in ob_img_temp:
ob_img.append(j)
for i in ob_img:
print [i.num,i.nom,i.ruta]
