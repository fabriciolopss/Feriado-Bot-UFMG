import re
import datetime

class Formatacao():
    def __init__(self):
        self.datas = []
        self.cidade = []
        self.diaDaSemana = []
        self.nomeFeriado = []
        self.data = datetime.datetime.now()
        self.diaMes = self.data.strftime("%d/%m")
        self.quantDiaMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.feriadosProximos = {}

    def read_document(self):
        with open ('src/feriados.txt', 'r', encoding = "utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if (line[0].isnumeric()): #checa se é a linha correspondente a data e cidade
                    self.datas.append(line[0:5]) #Extraindo data da linha correspondente
                    self.cidade.append(re.search(r'\((.*?)\)',line).group(1)) #Extraindo cidade da linha correspondente
                else:
                    divisao = line.split(", ") #dividindo a linha 2 em antes e depois da virgula
                    self.nomeFeriado.append(divisao[0]) #atribuindo valores com vetor gerado
                    self.diaDaSemana.append(divisao[1].strip('\n'))
        self.getClosest()

    def getClosest(self): #função responsável por pegar todos os feriados e calcular a distancia em dias até ele
        index = 0
        for x in self.datas:
            distancia = 0
            diaFeriado = int(x[0:2])
            diaAtual = int(self.diaMes[0:2])
            mesFeriado = int(x[3:5])
            mesAtual = int(self.diaMes[3:5])
            if(mesFeriado == mesAtual):
                if (diaAtual > diaFeriado):
                    distancia = 0
                else:
                    distancia = abs(diaAtual - diaFeriado)
            elif(mesAtual < mesFeriado):
                if(diaAtual > diaFeriado):
                    for x in range(mesAtual, mesFeriado):
                        distancia += self.quantDiaMeses[x - 1]
                    distancia -= diaAtual - diaFeriado
                else:
                    for x in range(mesAtual, mesFeriado):
                        distancia += self.quantDiaMeses[x - 1]
                    distancia += diaFeriado - diaAtual
            self.feriadosProximos[self.nomeFeriado[index]] = distancia
            index += 1
    
    def feriados(self):
        self.read_document()
        return self.feriadosProximos, self.diaDaSemana, self.datas, self.cidade, self.nomeFeriado


