import tweepy
from src.calendario import Formatacao
import os

class twitter():
    def __init__(self):
        self.consumerKey = os.environ['consumerKey']
        self.consumerSecret = os.environ['consumerSecret']
        self.acessToken = os.environ['acessToken']
        self.acessSecret = os.environ['acessSecret']
        self.tweetString = ""


    def tweetMaker(self):
        calendario = Formatacao()
        distanciaFeriados, diasDaSemana, datas, cidade, nomeFeriado = calendario.feriados()
        index = 0
        for x in nomeFeriado:
            if (0 < distanciaFeriados[x] < 30 and self.tweetString == ""):
                if(distanciaFeriados[x] == 1):
                    if (diasDaSemana[index] == "Domingo" or diasDaSemana[index] == "Sábado" ):
                        self.tweetString = "O feriado amanhã!! Infelizmente ele caiu em final de semana."
                    else:
                        self.tweetString = "O feriado começa amanhã, vamos comemorar!"
                else:
                    if (diasDaSemana[index] == "Domingo" or diasDaSemana[index] == "Sábado" ):  
                        if(cidade[index] == "Geral"):                
                            self.tweetString += "Faltam apenas {} dias para o próximo feriado ({}), que (infelizmente) cairá em um final de semana ({})."\
                            "\nEsse feriado é tanto pro campus Belo Horizonte quanto para Montes Claros. \n".format(distanciaFeriados[x], nomeFeriado[index], diasDaSemana[index])
                        else:
                            self.tweetString += "Faltam apenas {} dias para o próximo feriado ({}), que cairá em um dia de semana ({})."\
                            "\nEsse feriado é pro campus {}. \n".format(distanciaFeriados[x], nomeFeriado[index], diasDaSemana[index], cidade[index])                        
                    else:
                        if(cidade[index] == "Geral"):
                            self.tweetString += "Faltam apenas {} dias para o próximo feriado ({}), que cairá em um dia de semana ({}-feira)."\
                            "\nEsse feriado é tanto pro campus Belo Horizonte quanto para Montes Claros. \n".format(distanciaFeriados[x], nomeFeriado[index], diasDaSemana[index])
                        else:
                            self.tweetString += "Faltam apenas {} dias para o próximo feriado ({}), que cairá em um dia de semana ({}-feira)."\
                            "\nEsse feriado é pro campus {}. \n".format(distanciaFeriados[x], nomeFeriado[index], diasDaSemana[index], cidade[index])

            index += 1
        if(self.tweetString == ""):
            self.tweetString = "Não existe nenhum feriado nos próximos 30 dias :("
        print(self.tweetString)

    def useTwitter(self, auth):
        api = tweepy.API(auth)
        api.update_status(status = '{}'.format(self.tweetString))


    def loginTwitter(self):
        auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        auth.set_access_token(self.acessToken, self.acessSecret)
        self.tweetMaker()
        self.useTwitter(auth)


twettar = twitter()
twettar.loginTwitter()