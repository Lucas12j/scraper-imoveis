# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import os

#REVISAR CÓDIGO
#ZAP MUDOU A FORMA EM QUE E PASSADO OS PARAMETROS DO TAMANHO DO IMOVEL, NECESSARIA A ALTERACAO NA FORMACAO DA URL

class GetDataZap(object):

    def __init__(self, tipo, tipo_imovel, n_vagas, n_quartos, n_banheiros, tam_min, tam_max):
        self.table = [["PREÇO","ÁREA","N° QUARTOS", "N° VAGAS", "N° BANHEIRO","CONDOMÍNIO", "IPTU","DESCRIÇÃO", "ENDEREÇO"]]

        self.after = ""
        self.before = ""

        if tipo != "":
            if tipo == 1:
                self.before = self.before+"venda/"
            elif tipo == 2:
                self.before = self.before+"aluguel/"
        if tipo_imovel != "":
            if tipo_imovel == 1:
                self.before = self.before+"apartamentos/"
            if tipo_imovel == 2:
                self.before = self.before+"casas/"
            if tipo_imovel == 3:
                self.before = self.before+"loja-salao/"
            if tipo_imovel == 4:
                self.before = self.before+"conjunto-comercial-sala/"
            if tipo_imovel == 5:
                self.before = self.before+"terrenos-lotes-condominios/"
            if tipo_imovel == 6:
                self.before = self.before+"casas-de-condominio/"
            if tipo_imovel == 7:
                self.before = self.before+"cobertura/"
            
        if n_vagas != "":
            self.after = self.after+"&vagas="+n_vagas
        if n_quartos != "":
            self.after = self.after+"&quartos="+n_quartos
        if n_banheiros != "":
            self.after = self.after+"&banheiros="+n_banheiros
        if tam_max != "":
            self.after= self.after+"&areaMaxima="+tam_max
        if tam_min != "":
            self.after= self.after+"&areaMinima="+tam_min

    def getData(self, local):
        
        counter = 1
        while True:     
            url = "https://www.zapimoveis.com.br/"+self.before+local+"?pagina="+str(counter)+self.after
            agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
            r = requests.get(url, headers=agent)
            soup = BeautifulSoup(r.text, 'lxml')    

            if "Oops" in str(soup.select(".results__wrapper h1 strong")) or "Ops" in str(soup.select("#app h3 strong")):
                break
            else:
                for i in range(2,27):
                    preco = self.data_cleaner(str(soup.select(".card-container:nth-child("+str(i)+") strong")).replace(" ",""))
                    area = self.data_cleaner(str(soup.select(".card-container:nth-child("+str(i)+") .js-areas span:nth-child(2)")).replace(" ",""))
                    n_quarto= self.data_cleaner(str(soup.select(".card-container:nth-child("+str(i)+") .js-bedrooms span:nth-child(2)")).replace(" ",""))
                    n_vaga = self.data_cleaner(str(soup.select(".card-container:nth-child("+str(i)+") .js-parking-spaces span:nth-child(2)")).replace(" ",""))
                    n_banheiro = self.data_cleaner(str(soup.select(".card-container:nth-child("+str(i)+") .js-bathrooms span:nth-child(2)")).replace(" ",""))
                    condominio = self.data_cleaner(str(soup.select(".card-container:nth-child("+str(i)+") .condominium span")).replace(" ",""))
                    iptu = self.data_cleaner(str(soup.select(".card-container:nth-child("+str(i)+") .iptu span")).replace(" ",""))
                    descricao = self.data_cleaner(str(soup.select(".card-container:nth-child("+str(i)+") .simple-card__text")))
                    endereco = self.data_cleaner(str(soup.select(".card-container:nth-child("+str(i)+") .simple-card__address")))
                    self.table.append([preco.replace("\n",""),area.replace("\n",""),n_quarto.replace("\n",""),n_vaga.replace("\n",""),n_banheiro.replace("\n",""),condominio.replace("\n",""),iptu.replace("\n",""),descricao,endereco])
                print(f"\nDados da página {counter} de {local[0]+local[1]} coletados")
                counter += 1                
                
        self.create_csv(local)
        

    def create_csv(self, local):
        if "rj" in local:
            with open('imoveis_Zap_RJ.csv', 'w', newline='', encoding='utf-8') as csvfile:
                file_csv = csv.writer(csvfile)
                for i in self.table:
                    file_csv.writerow(i)
        elif "sp" in local:
            with open('imoveis_Zap_SP.csv', 'w', newline='', encoding='utf-8') as csvfile:
                file_csv = csv.writer(csvfile)
                for i in self.table:
                    file_csv.writerow(i)
    def data_cleaner(self, data):
        data_cleaned = ""
        check1 = False
        check2 = False
        data = data.replace("<br/>","")

        for i in data:
            if i == ">":
                check1 = True
            if i == "<" and check1 == True:
                check2 = True

            if check1 == True and check2 == False:
                data_cleaned = data_cleaned+i
        return (data_cleaned.replace(">",""))


