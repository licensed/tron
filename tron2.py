# -*- coding: utf-8 -*-
#Tron: O Perceptron

import matplotlib.pyplot as plt
from time import sleep
from blessings import Terminal

t = Terminal()
class Tron:
    f = open("data.txt","r")
    sensores = f.read().split('\n')
    sensores = sensores[:100] + sensores[200:] #Limita a base de treinamento em 100 entradas de cada classe
    base_teste = sensores[:50] + sensores[150:] #Limita a base de teste em 50 entradas de cada classe
    f.close()
    b = 1 #Bias
    a = 0.1 #Taxa de aprendizagem
    naomudou = 0 #Contador de parada
    th = 0.5 #Limiar
    x = sensores[0].split(' ') #['0.1111', 0.2222', '1'] #Primeiros pontos + saida desejada
    z = int(x[-1]) #Saida desejada
    #pesos = [0,0,0] #Pesos Iniciais
    s = 0 #Soma das saidas
    n = 0 #Degrau 0 ou 1
    e = z - n #Erro (saida desejada - saida obtida)
    d = a * e #Correcao (taxa de aprendizagem * erro)
    pesosfinais = [0,0,0]
    errou = False

    def treina(self, pesos=[0,0,0]):
        print t.blue("TREINANDO")
        plt.title("PERCEPTRON")
        self.pesos = pesos
        self.errou = False
        self.naomudou = 0
        for sensor in self.sensores:
            if pesos != [0,0,0]:
                w0 = pesos[0]
                w1 = pesos[1]
                w2 = pesos[2]
            else:
                w0 = self.pesos[0] + (self.a * self.b * self.e)
                w1 = self.pesos[1] + (self.a * float(self.x[0]) * self.e)
                w2 = self.pesos[2] + (self.a * float(self.x[1]) * self.e)
            pf = [w0,w1,w2]
            self.pesosfinais = pf            
            if self.pesosfinais == self.pesos: #Se não houve alteração de pesos
                if self.naomudou > 200: #Se os pesos se mantem por mais de 3x
                    return pf #Retorna os pesos finais para desenhar a reta
                self.naomudou = self.naomudou + 1
            else:
                self.naomudou = 0
            self.x = sensor.split(' ') #Atualiza os sensores
            self.z = int(self.x[-1]) #Atualiza a saida desejada
            self.pesos = pf #Atualiza pesos
            c0 = self.b * self.pesos[0]
            c1 = float(self.x[0]) * self.pesos[1]
            c2 = float(self.x[1]) * self.pesos[2]
            self.s = c0+c1+c2 #Atualiza a soma das saidas
            if self.s > self.th: #Atualiza a network (Funcao degrau)
                self.n = 1
            else:
                self.n = 0
            self.e = self.z - self.n #Atualiza o erro
            self.d = self.th * self.e #Atualiza a correcao
            if self.e != 0:
                self.errou = True
            sleep(0.03)
            if self.z != self.n:
                print t.red("!ERRO! %s Desejada: %s Obtida: %s" % (sensor,self.z,self.n))
            else:
                print t.white("!ACERTO! %s Desejada: %s Obtida: %s" % (sensor,self.z,self.n))
        if self.errou: #Enquanto houver erro, chama a funcao de treino recursivamente
            self.treina(pesos=pf)
        else: #Quando finaliza o treino, pega os pesos finais e plota a reta
            xx = [-3,3]
            yy = []
            for n in xx:
                yy.append( (self.th/pesos[2]) - (pesos[0]/pesos[2]) - (pesos[1]/pesos[2]*n) )
                #yy.append((self.th - pesos[2] - n * pesos[0]) / pesos[1])
            plt.plot(yy,xx,'--k')   #fazer o gráfico dos dois vectores.
            self.pesos = pf            
            return self.pesos

           
        #plt.axis([-1,1,-1,1])        
        #FORMULA: x1 = ( th + w2 - x2 * w0 ) / w1
        #y1 = (self.th - w[2] - x1 * w[0]) / w[1]
        
        
        
        
    def testa(self, pf): #Funcao que testa a base
        self.pesos = pf
        self.errou = False
        self.naomudou = 0
        for sensor in self.base_teste:
            sleep(0.02)
            self.x = sensor.split(' ') #Atualiza os sensores
            self.z = int(self.x[-1]) #Atualiza a saida desejada
            c0 = self.b * self.pesos[0]
            c1 = float(self.x[0]) * self.pesos[1]
            c2 = float(self.x[1]) * self.pesos[2]
            self.s = c0+c1+c2 #Atualiza a soma das saidas
            if self.s > self.th: #Atualiza a network (Funcao degrau)
                self.n = 1
            else:
                self.n = 0
            self.e = self.z - self.n #Atualiza o erro
            if self.z != self.n:
                print t.red("!ERRO! %s Desejada: %s Obtida: %s" % (sensor,self.z,self.n))
            else:
                print t.white("!ACERTO! %s Desejada: %s Obtida: %s" % (sensor,self.z,self.n))
        
        
        
        
    def plota(self):
        #print self.base_teste[0].split(' ')[:2]
        plt.ion()
        lis = []
        for p in self.base_teste:
            x = float(p.split(' ',2)[0])
            y = float(p.split(' ',2)[1])
            z = float(p.split(' ',2)[2])
            if z == 1.0:
                plt.plot(x,y,marker='.',color='black')
            else:
                plt.plot(x,y,marker='.',color='red')
        
        plt.plot([-3,3],[0,0],marker='.',color='black')  #tentar criar linhas
        plt.plot([0,0],[-3,3],marker='.',color='black') #para os eixos X e Y.
        plt.ylim(-3,3)  #limitar a janela dos gráficos em Y.
        plt.xlim(-3,3)  #e em X.
        plt.show()    #Mostra o grafico final
        #k = (self.th - pf[2] - n * pf[0]) / pf[1] #1a tentativa de acordo com wikipedia
        

tron = Tron()
tron.plota()
tron.treina()
qq = raw_input("Base treinada. Testar? [s/N]")
if qq.lower() == 's':
    tron.testa(tron.pesosfinais)
sair = raw_input("Pressione para sair")