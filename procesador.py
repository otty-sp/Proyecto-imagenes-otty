    class procesador:
             
             #libreria.txt
 
    def txt_nombre(self):
        fila1 = open(self.fila_path + '/img_directorio.txt', 'r')
        nombre = []
        for i in file1:
            i = i.rstrip().split('|')
            nombre.append(i[0])
        return nombre

    def cargar_libreria(self):
        paths = [self.file_path + '/img_directorio.txt', self.fila_path + '/image_libreria/img_map.txt']
        if os.path.isdir(self.fila_path + '/image_libreria'):
            pass
        else:
            os.mkdir(self.file_path + '/image_libreria')
        for i in paths:
            if os.path.isfile(i):
                file1 = open(i, 'r')
                for j in file1:
                    j = j.rstrip().split('|')
                    self.dic.append(Img(j[0], j[1], j[2], j[3]))
                    self.idi += 1
                file1.close()
            else:
                open(i, 'w').close()
                
                
