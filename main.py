from fbs_runtime.application_context.PySide2 import ApplicationContext
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QApplication
#pantallas
from pantalla_calculo_std import Ui_MainWindow
from intro_std import Ui_Intro
from pantalla_calculo_low import Ui_MainWindow_low
from intro_low import Ui_Intro_low

g_numeros = []
sendero_mun_v = ''
res = ''

class intro(QMainWindow):
    def __init__(self):
        global res
        QMainWindow.__init__(self)
        ##print(res)
        if res == 'std':
            self.ui = Ui_Intro()
        else: 
            self.ui = Ui_Intro_low()
            
        self.ui.setupUi(self)
         
        self.ui.ingresar.clicked.connect(self.fn_cargar_app)
        self.ui.salir.clicked.connect(self.fn_boton_salir)
        self.ui.cambiar_res.clicked.connect(self.fn_boton_cambiar_res)

    def fn_cargar_app(self):
        self.main = aplicacion()
        self.main.show()

        self.close()

    def fn_boton_salir(self):
        sys.exit()
    
    def fn_boton_cambiar_res(self):
        global res
        if res == 'std':
            res = 'low'
        else:
            res = 'std'
        
        self.main = intro()
        self.main.show()
        self.close()

class aplicacion(QMainWindow):

    def __init__(self):
     
        super(aplicacion, self).__init__()
        if res == 'std':
            self.ui = Ui_MainWindow()
        else:
            self.ui = Ui_MainWindow_low()
            
        self.ui.setupUi(self)

        self.ui.boton_calc.clicked.connect(self.fn_boton_calcular_nom) #para pasar la acción al clickear
        self.ui.boton_calc_anio.clicked.connect(self.fn_boton_calcular_anio)
        self.ui.salir.clicked.connect(self.fn_boton_salir)
        
    def fn_boton_salir(self):
        sys.exit()
        
    def fn_boton_calcular_nom(self):
        self.inicializar()
        nombres=self.ui.nombres.text() 
        apellidos=self.ui.apellidos.text()
        if len(nombres+apellidos) == 0:
            self.ui.ingrese_nombre.setText('Debe ingresar Nombre/s y Apellido/s')
        else:
            self.ui.ingrese_nombre.setText('')
            self.fn_calcular_nom()

    def fn_boton_calcular_anio(self):
        anio=self.ui.anio.text()
        if len(anio) == 0:
            self.ui.ingrese_anio.setText('Debe ingresar un año válido')
        else:
            self.ui.ingrese_anio.setText('')
            self.fn_calcular_anio()

    def fn_calcular_nom(self):
        #calcula clave personal
        fecha_nac=str(self.ui.fecha_nac.date().toPython()) #devuelve YYYY-MM-DD
        dia_nac=fecha_nac[8:10]
        mes_nac=fecha_nac[5:7]
        
        dia_mes=dia_nac+mes_nac
        self.ui.clave_personal.setText(str(self.valor_dia(dia_mes)))    

        #separo los nombres y apellidos
        nombres=self.ui.nombres.text().split() #armo listas de strings de cada nombre
        apellidos=self.ui.apellidos.text().split()
       
        if len(apellidos) == 0:
            self.ui.imagen.setText('None')
        else:
            self.ui.imagen.setText(apellidos[0]) 
        
        #cálculos relacionados con el nombre
        self.valor_letra(nombres,apellidos)
        sendero_n = self.sendero_natal(fecha_nac)
        self.etapas(sendero_n)
        self.potencial(sendero_n)
        self.lecciones_karmicas()

    def inicializar(self):
        global g_numeros
        global sendero_mun_v

        #self.ui.esencia_k.setText(' ')
        #self.ui.sendero_nat_k.setText(' ')
        self.ui.anio_personal.setText(' ')
        self.ui.anio_personal_v.setText(' ')
        self.ui.digito_edad.setText(' ')
        self.ui.digito_edad_v.setText(' ')
        self.ui.lecciones_karmicas.setText(' ')
        g_numeros.clear()
        sendero_mun_v=''

    def sendero_natal(self,fecha_nac):
        dia_nac=fecha_nac[8:10]
        mes_nac=fecha_nac[5:7]
        anio_nac=fecha_nac[0:4]

        #calculo karmas
        sendero_nat_k=[0,'',0,'']    
        if dia_nac != '11':
            dia_nac=self.reducir_v(dia_nac)
        #print(dia_nac)
        if mes_nac != '11':
            mes_nac = self.reducir_v(mes_nac)
        #print(mes_nac)
        anio_nac = self.reducir_tot(anio_nac)
        #print(anio_nac)

        #sendero_nat_k = self.calcular_karma_s([self.reducir_v(dia_nac),self.reducir_v(mes_nac),self.reducir_v(anio_nac)],sendero_nat_k)
        sendero_nat_k = self.calcular_karma_s([dia_nac,mes_nac,anio_nac],sendero_nat_k)
        
        #self.ui.sendero_nat_k.setText(sendero_nat_k[3])
        self.ui.sendero_nat.setText(str(sendero_nat_k[0])+' '+sendero_nat_k[1]+' '+sendero_nat_k[3])

        return sendero_nat_k[0]

    def potencial(self, sendero_n):

        valores_k=[0,'',0,'']    
        valores_k = self.calcular_karma([sendero_mun_v,str(sendero_n)],valores_k)
        self.ui.potencial.setText(self.reducir_v([sendero_mun_v,sendero_n])+' '+valores_k[1])
        #self.ui.potencial.setText(self.reducir_v(str(int(sendero_mun_v)+int(sendero_n)))+valores_k[1])

    def lecciones_karmicas(self):
        numeros = ['1','2','3','4','5','6','7','8','9']

        for n in g_numeros:
            try: 
                numeros.remove(str(n))
            except: #ya la saqué
                pass                
        
        lecciones = self.armar_lecciones(numeros)
        self.ui.lecciones_karmicas.setText(' '.join(lecciones))

    def valor_letra(self, nombres, apellidos):
        #función que obtiene el valor de las letras del nombre
        global g_numeros
        global sendero_mun_v

        vocales = {
            'A':1,'Á':1,'E':5,'É':5,'I':9,'Í':9,'O':6,'Ó':6,'U':3,'Ú':3
        }
        consonantes = {
            'B':2,'C':3,'D':4,'F':6,'G':7,'H':8,'J':1,'K':2,'L':3,'M':4,'N':5,'Ñ':5,'P':7,'Q':8,'R':9,'S':1,'T':2,'V':4,'W':5,'X':6,'Y':7,'Z':8
        }

        voc = []
        cons = []
        suma_v = []
        suma_c = []

        cant_letras = 0

        esencia = []
        imagen = []
        sendero_m = []
        total = []

        nombre_completo = nombres + apellidos

        for n in nombre_completo:
            cant_letras = cant_letras + int(len(n))
            voc.clear()
            cons.clear()
            for l in n.upper():
                try: #pruebo con vocal
                    letra = vocales[l]
                    voc.append(letra)
                    g_numeros.append(letra)
                except: 
                    try: #pruebo con consonante
                        letra = consonantes[l]
                        cons.append(letra)
                        g_numeros.append(letra)
                    except:
                        #no es letra
                        pass
            suma_v.append(self.reducir_v10(voc))
            suma_c.append(self.reducir_v10(cons))
            
        #ciclo de letras
        self.ui.ciclo_letras.setText(str(cant_letras))

        aux=[]
        #armo esencia, imagen y sendero del mundo
        esencia = self.calcular_sentencia(suma_v, aux)
        imagen = self.calcular_sentencia(suma_c, aux)
        sendero_m = self.calcular_sentencia(esencia,imagen)

        #calculo karmas
        esencia_k=[0,'',0,'']    
        esencia_k = self.calcular_karma(esencia,esencia_k)
        
        total = []
        indice=0
        var=''
        for n in esencia:
            sendero_m_k=[0,'',0,'']
            sendero_m_k=self.calcular_karma([n,imagen[indice]],sendero_m_k)
            var=sendero_m_k[1]+sendero_m_k[3]
            if len(var): total.append(var)
            else: total.apend('  ')
            indice = indice + 1

        sendero_m_k = self.calcular_karma(sendero_m,sendero_m_k)
        
        #completo valores de esencia, imagen y sendero del mundo
        esencia_v = self.reducir_sentencia(esencia)+' '+esencia_k[1]
        imagen_v = self.reducir_sentencia(imagen)
        sendero_mun_v = self.reducir_sentencia(sendero_m)
        
        #completo datos de esencia, imagen, sendero del mundo y total
        self.ui.esencia.setText(self.armar_sentencia(esencia,0)+' = '+esencia_v+' '+esencia_k[3])
        self.ui.imagen.setText(self.armar_sentencia(imagen,0)+' = '+imagen_v)
        self.ui.sendero_mun.setText(self.armar_sentencia(sendero_m,0)+' = '+sendero_mun_v+' '+sendero_m_k[1]+' '+sendero_m_k[3])
        self.ui.total.setText(self.armar_sentencia(total,1))

    def calcular_sentencia(self,lista1,lista2):
        resultado=[]
        indice=0
        var=0
        if len(lista2):
            for n in lista1:
                var=self.reducir(str(int(n)+int(lista2[indice])))
                if var == '10': var='1'
                resultado.append(var)
                indice = indice + 1
        else:
            for n in lista1:
                resultado.append(self.reducir(str(n)))
        return resultado

    def armar_sentencia(self,lista,total):
        resultado=['( ']
        indice=0

        for n in lista:
            if indice > 0:
                if total==0: resultado.append(' - ')                
                else: resultado.append('- ') 
            else:
                indice=1
            if n == '0':
                resultado.append('   ')
            else:
                if len(n) == 1: resultado.append(' ')
                if total == 1: 
                    if len(n) == 3: resultado.append('    ')
                    else: resultado.append('')
                resultado.append(n)
        resultado.append(' )')
        return ' '.join(resultado)

    def armar_lecciones(self,lista):
        resultado=['']
        indice=0

        for n in lista:
            if indice > 0:
                resultado.append('-')                
            else:
                indice=1
            resultado.append(n)
        return ' '.join(resultado)

    def reducir(self, numero):
        suma=0
        if numero == '10' or numero == '11' or numero == '22':
            return numero
        else:
            for n in numero:
                suma=suma+int(n)
            return str(suma)
    
    def reducir_sentencia(self,lista):
        suma=0
        valor=''        
        #caso especial 33
        once = lista.count('11')
        ventidos = lista.count('22')
        cant = len(lista)
        #print(lista)
        if once == 3 and cant == 3:
            return '33'
    
        for numero in lista:
            if numero != '11' and numero != '22':
                if numero == '10': suma = suma+1
                else: suma = suma + int(numero)
               
        if suma == 11 or suma == 22:
            valor = suma
        else:
            valor = self.reducir(str(suma))
        suma = int(valor) + 11*once + 22*ventidos
        #print(suma)
        if suma == 11 or suma == 22: return str(suma)
        else: return self.reducir_tot(str(suma))
        
    
    def reducir_tot(self, numero):
        suma=0
        for n in numero:
            suma=suma+int(n)
        if len(str(suma)) > 1 and suma != 11:
            suma=int(self.reducir_tot(str(suma)))
        return str(suma)

    def reducir_v(self, lista):
        suma=0
        valor=0
        #caso especial 33
        once = lista.count('11')
        cant = len(lista)
        
        if once == 3 and cant == 3:
            return '33' 

        for numero in lista:
            #si la lista que mando es numérica, tengo que transformar a caracter
            try:
                valor=valor+numero
            except:
                valor=valor+int(numero)

        if str(valor) == '11' or str(valor) == '22':
            return str(valor)
        else:
            for n in str(valor):
                suma=suma+int(n)
            if len(str(suma)) > 1:
                if suma != 11 and suma != 22:
                    suma=int(self.reducir_v(str(suma)))
            return str(suma)
            
    def reducir_v10(self, lista):
        suma=0
        valor=0
        #caso especial 33
        once = lista.count('11')
        cant = len(lista)
        if once == 3 and cant == 3:
            return '33' 

        for numero in lista:
            #si la lista que mando es numérica, tengo que transformar a caracter
            try:
                valor=valor+numero
            except:
                valor=valor+int(numero)
        
        if str(valor) == '11' or str(valor) == '22' or str(valor) == '10':
            return str(valor)
        else:
            for n in str(valor):
                suma=suma+int(n)
            if len(str(suma)) > 1:
                if suma != 11 and suma != 22 and suma!=10:
                    suma=int(self.reducir_v(str(suma)))
            return str(suma)
            
    def reducir_etapa(self, lista):
        suma=0
        valor=0
        #print(lista)
        once = lista.count('11')
        #print('once: '+str(once))
        cant = len(lista)
        if once == 2: return '22'
        
        if lista == '11' :
            return lista
        else:
            for n in lista:
                suma=suma+int(n)
            #print('suma:'+str(suma))
            if len(str(suma)) > 1:
                #print('if1 '+str(suma))
                if suma != 11 and suma != 22:
                    #print('if2 '+str(suma))
                    suma=int(self.reducir_v(str(suma)))
            return str(suma)
    
    def calcular_karma(self,valores,valores_k):
        vuelta=1
        once=0
        for n in valores:
            if vuelta == 1:
                if n != '11' and n !='22':
                    valores_k[0]=int(n)
                    vuelta=2
                    valores_k[2]=0
                else:
                    #valores_k[2]=int(self.reducir(n))
                    valores_k[2]=int((n))
                    valores_k[0]=0
                    vuelta=2
            else:
                if n != '11' and n !='22':
                    valores_k[0]=valores_k[0]+int(n)
                else:
                    #valores_k[2]=valores_k[2]+int(self.reducir(n))
                    valores_k[2]=valores_k[2]+int((n))
        
        if valores_k[0] == 13 or valores_k[0] == 14 or valores_k[0] == 16 or valores_k[0] == 19:
            valores_k[1]='K'+str(valores_k[0])
        else:
            valores_k[1]='  '
        #valores_k[2]=self.reducir_tot(str(valores_k[2]))
        valores_k[0]=int(self.reducir(str(valores_k[0])))+int(valores_k[2])
        
        if (valores_k[0] == 13 or valores_k[0] == 14 or valores_k[0] == 16 or valores_k[0] == 19) and valores_k[1] != ('K'+str(valores_k[0])):
            valores_k[3]=('K'+str(valores_k[0]))
        else:
            valores_k[3]=' '
        
        return valores_k

    def calcular_karma_s(self,valores,valores_k):
        vuelta=1
        valores_k[2]=0
        
        for n in valores:
            if vuelta == 1:
                if n != '11' and n!='22' :
                    valores_k[0]=int(n)
                    vuelta=2                    
                else:
                    #valores_k[2]=int(self.reducir(n))
                    valores_k[2]=int(n)
            else:
                if n != '11' and n!='22':
                    valores_k[0]=valores_k[0]+int(n)
                else:
                    #valores_k[2]=valores_k[2]+int(self.reducir(n))
                    valores_k[2]=valores_k[2]+int(n)
        
        if valores_k[0] == 13 or valores_k[0] == 14 or valores_k[0] == 16 or valores_k[0] == 19:
            valores_k[1]='K'+str(valores_k[0])
        else:
            valores_k[1]=' '
        
        if valores_k[0] == 11:
            aux = 11
        else:
            if valores_k[0] == 22:
                aux = 22
            else: 
                aux = int(self.reducir_v(str(valores_k[0])))
        
        if valores_k[2] == 11:
            aux = aux + 11
        else:
            if valores_k[2] == 22:
                aux = aux + 22
            else: 
                aux = aux + int(self.reducir_v(str(valores_k[2])))
        #aux=int(self.reducir_v(str(valores_k[0])))+int(self.reducir_v(str(valores_k[2])))
             
        if (aux == 13 or aux == 14 or aux == 16 or aux == 19) and valores_k[1] != ('K'+str(aux)):
            valores_k[3]=('K'+str(aux))
        else:
            valores_k[3]=' '
            
        #print('k0'+str(valores_k[0]))
        #print('k2'+str(valores_k[2]))
        #print('aux'+str(aux))        
        valores_k[0]=aux

        if valores_k[0] == 11 or valores_k[0] == 22:
            return valores_k
        else:
            valores_k[0]=self.reducir_v(str(aux))
            return valores_k
                

    def valor_dia(self,dia):
        #función que obtiene el valor del día del año
        dias ={ 
            #enero
            '0101':9,'0201':8,'0301':2,'0401':9,'0501':10,'0601':2,'0701':3,'0801':4,'0901':5,'1001':6,
            '1101':7,'1201':8,'1301':9,'1401':8,'1501':9,'1601':10,'1701':11,'1801':3,'1901':4,'2001':2,
            '2101':3,'2201':4,'2301':5,'2401':13,'2501':5,'2601':6,'2701':4,'2801':5,'2901':6,'3001':7,'3101':8,
            #febrero
            '0102':10,'0202':8,'0302':9,'0402':10,'0502':2,'0602':3,'0702':4,'0802':5,'0902':6,'1002':7,
            '1102':8,'1202':7,'1302':8,'1402':9,'1502':10,'1602':11,'1702':3,'1802':4,'1902':2,'2002':3,
            '2102':4,'2202':1,'2302':4,'2402':5,'2502':12,'2602':4,'2702':5,'2802':6,'2902':7,
            #marzo
            '0103':5,'0203':6,'0303':7,'0403':8,'0503':9,'0603':10,'0703':2,'0803':3,'0903':4,'1003':3,
            '1103':4,'1203':5,'1303':6,'1403':7,'1503':8,'1603':9,'1703':10,'1803':11,'1903':3,'2003':11,
            '2103':9,'2203':10,'2303':8,'2403':9,'2503':10,'2603':2,'2703':3,'2803':4,'2903':5,'3003':5,'3103':6,
            #abril
            '0104':6,'0204':7,'0304':8,'0404':9,'0504':10,'0604':2,'0704':3,'0804':2,'0904':3,'1004':4,
            '1104':5,'1204':6,'1304':7,'1404':8,'1504':9,'1604':10,'1704':11,'1804':10,'1904':11,'2004':9,
            '2104':7,'2204':8,'2304':9,'2404':10,'2504':11,'2604':3,'2704':4,'2804':4,'2904':5,'3004':6,
            #mayo
            '0105':6,'0205':7,'0305':8,'0405':9,'0505':10,'0605':9,'0705':1,'0805':2,'0905':3,'1005':4,
            '1105':5,'1205':6,'1305':7,'1405':8,'1505':9,'1605':8,'1705':9,'1805':10,'1905':8,'2005':6,
            '2105':7,'2205':8,'2305':9,'2405':1,'2505':11,'2605':11,'2705':3,'2805':4,'2905':5,'3005':6,'3105':8,
            #junio
            '0106':7,'0206':8,'0306':9,'0406':8,'0506':9,'0606':10,'0706':2,'0806':3,'0906':4,'1006':5,
            '1106':6,'1206':7,'1306':8,'1406':7,'1506':8,'1606':9,'1706':7,'1806':8,'1906':6,'2006':6,
            '2106':7,'2206':7,'2306':8,'2406':7,'2506':8,'2606':8,'2706':9,'2806':9,'2906':1,'3006':8,
            #julio
            '0107':11,'0207':1,'0307':11,'0407':3,'0507':4,'0607':5,'0707':6,'0807':7,'0907':8,'1007':9,
            '1107':10,'1207':9,'1307':10,'1407':11,'1507':9,'1607':10,'1707':11,'1807':3,'1907':4,'2007':5,
            '2107':6,'2207':6,'2307':7,'2407':5,'2507':6,'2607':7,'2707':8,'2807':8,'2907':7,'3007':6,'3107':5,
            #agosto
            '0108':10,'0208':11,'0308':3,'0408':4,'0508':5,'0608':6,'0708':7,'0808':8,'0908':9,'1008':8,
            '1108':9,'1208':10,'1308':8,'1408':9,'1508':10,'1608':11,'1708':3,'1808':4,'1908':5,'2008':5,
            '2108':6,'2208':7,'2308':5,'2408':6,'2508':7,'2608':9,'2708':8,'2808':7,'2908':8,'3008':5,'3108':4,
            #septiembre
            '0109':11,'0209':3,'0309':4,'0409':5,'0509':6,'0609':7,'0709':8,'0809':7,'0909':8,'1009':9,
            '1109':7,'1209':8,'1309':9,'1409':10,'1509':11,'1609':3,'1709':4,'1809':4,'1909':5,'2009':6,
            '2109':7,'2209':5,'2309':6,'2409':1,'2509':9,'2609':8,'2709':7,'2809':8,'2909':11,'3009':4,
            #octubre
            '0110':11,'0210':3,'0310':4,'0410':5,'0510':6,'0610':5,'0710':6,'0810':7,'0910':5,'1010':6,
            '1110':7,'1210':8,'1310':9,'1410':10,'1510':11,'1610':11,'1710':3,'1810':4,'1910':5,'2010':6,
            '2110':7,'2210':1,'2310':9,'2410':8,'2510':7,'2610':6,'2710':7,'2810':1,'2910':4,'3010':11,'3110':1,
            #noviembre
            '0111':3,'0211':4,'0311':5,'0411':4,'0511':5,'0611':6,'0711':4,'0811':5,'0911':6,'1011':7,
            '1111':8,'1211':9,'1311':10,'1411':10,'1511':11,'1611':3,'1711':4,'1811':5,'1911':6,'2011':5,
            '2111':1,'2211':9,'2311':8,'2411':7,'2511':6,'2611':7,'2711':1,'2811':4,'2911':7,'3011':1,
            #diciembre
            '0112':3,'0212':2,'0312':3,'0412':4,'0512':2,'0612':3,'0712':4,'0812':5,'0912':6,'1012':7,
            '1112':8,'1212':8,'1312':9,'1412':10,'1512':11,'1612':3,'1712':4,'1812':5,'1912':6,'2012':12,
            '2112':8,'2212':7,'2312':6,'2412':5,'2512':6,'2612':9,'2712':3,'2812':6,'2912':9,'3012':3,'3112':4
        }

        valor=dias[dia]
        return valor

    def fn_calcular_anio(self):
        anio=self.ui.anio.text()
        
        #calcula año personal
        fecha_nac=str(self.ui.fecha_nac.date().toPython()) #devuelve YYYY-MM-DD
        dia_nac=fecha_nac[8:10]
        mes_nac=fecha_nac[5:7]
        anio_nac=fecha_nac[0:4]
        
        if int(anio) < int(anio_nac):
            self.ui.ingrese_anio.setText('El año debe ser mayor a la fecha de nacimiento')
        else:
            try: 
                self.ui.anio_personal.setText(self.reducir_v(dia_nac)+' + '+self.reducir_v(mes_nac)+' + '+self.reducir_v(anio)+' = ')
                self.ui.anio_personal_v.setText(self.reducir_v(str(int(self.reducir_v(dia_nac))+int(self.reducir_v(mes_nac))+int(self.reducir_v(anio)))))
    
                #calculo digito de edad
                edad=int(anio)-int(anio_nac)-1
                self.ui.digito_edad.setText(str(edad)+' + '+str(edad+1)+' = ')
                self.ui.digito_edad_v.setText(self.reducir_v(str(edad+edad+1)))
            except: #no hay nros
                self.ui.ingrese_anio.setText('Ingrese un año válido')
        

    def etapas(self, sendero_nat):
        fecha_nac=str(self.ui.fecha_nac.date().toPython()) #devuelve YYYY-MM-DD
        dia_nac=fecha_nac[8:10]
        mes_nac=fecha_nac[5:7]
        anio_nac=fecha_nac[0:4]
        anio_nac=self.reducir_v(anio_nac)
        
        sendero_natal=self.ui.sendero_nat.text()
   
        #if sendero_natal == '1 K19':
        if 'K19' in sendero_natal:
            duracion_etapa = 26
        else:
            duracion_etapa= 36 - int(sendero_nat)
        etapa_1 = 'de 00 a ' + str(duracion_etapa) + ' = '
        etapa_2 = 'de ' + str(duracion_etapa+1)+' a '+ str(duracion_etapa+10) + ' = '
        etapa_3 = 'de ' + str(duracion_etapa+11)+' a '+ str(duracion_etapa+20) + ' = '
        etapa_4 = 'de ' + str(duracion_etapa+21)+' a ...' + ' = '

        self.ui.etapa_1.setText(etapa_1)
        self.ui.etapa_2.setText(etapa_2)
        self.ui.etapa_3.setText(etapa_3)
        self.ui.etapa_4.setText(etapa_4)

#nuevo reducir, donde solo se deja el 11
        #print('etapa 1')
        etapa_1_v=int(self.reducir_etapa([self.reducir_etapa(dia_nac),self.reducir_etapa(mes_nac)])) 
        #etapa_2_v=int(self.reducir_etapa([dia_nac,anio_nac]))
        #etapa_4_v=int(self.reducir_etapa([mes_nac,anio_nac]))
        
        #etapa_1_v=int(self.reducir_etapa(str(int(self.reducir_etapa(dia_nac))+int(self.reducir_etapa(mes_nac)) )))
        #print('etapa 2')
        
        etapa_2_v=int(self.reducir_etapa(str(int(self.reducir_etapa(dia_nac))+int(self.reducir_etapa(anio_nac)))))
        #print('etapa 4')
        
        etapa_4_v=int(self.reducir_etapa(str(int(self.reducir_etapa(mes_nac))+int(self.reducir_etapa(anio_nac)))))
        
        self.ui.etapa_1_v.setText((str(etapa_1_v)))
        self.ui.etapa_2_v.setText((str(etapa_2_v)))
        #print('etapa 3')
        
        self.ui.etapa_3_v.setText(self.reducir_etapa([str(etapa_1_v),str(etapa_2_v)]))
        self.ui.etapa_4_v.setText(str(etapa_4_v))


if __name__ == '__main__':
    
    res = 'std'
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    #app = QApplication(sys.argv)
    #GUI = aplicacion()
    GUI = intro()
    GUI.show()

    #sys.exit(app.exec_())
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)