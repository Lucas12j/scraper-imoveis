# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import os

class GetDataBrasilBrokers(object):

    def __init__(self, tipo, tipo_imovel, n_vagas, n_quartos, n_banheiros, tam_min, tam_max):
        self.table = [["PREÇO","ÁREA","N° QUARTOS", "N° VAGAS", "N° BANHEIRO", "TÍTULO","DESCRIÇÃO"]]

        self.after = ""
        self.before = ""

        if tipo != "":
            if tipo == 1:
                self.before=self.before+"mercado=pronto&"
            elif tipo == 2:
                self.before = self.before+"mercado=alugar&"
        if tipo_imovel != "":
            if tipo_imovel == 1:
                self.before = self.before+"tipologia=apartamento&"
            if tipo_imovel == 2:
                self.before = self.before+"tipologia=casa&"
            if tipo_imovel == 3:
                self.before = self.before+"tipologia=sala-loja-ou-conjunto-comercial&"
            if tipo_imovel == 4:
                self.before = self.before+"tipologia=sala-loja-ou-conjunto-comercial&"
            if tipo_imovel == 5:
                self.before = self.before+"tipologia=terreno-ou-loteamento-residencial&"
            if tipo_imovel == 6:
                self.before = self.before+"tipologia=casa-ou-terreno-em-condominio&"
            if tipo_imovel == 7:
                self.before = self.before+"tipologia=cobertura&"
            
        if n_vagas != "":
            self.after =self.after+ "vaga="+n_vagas+"&"
        if n_quartos != "":
            self.after = self.after+"dormitorio="+n_quartos+"&"
        if n_banheiros != "":
            self.after = self.after+"banheiro="+n_banheiros+"&"

        if tam_max == "":
            tam_max = "infinito"
        if tam_min == "":
            tam_min = "0"

        self.after = self.after+"area="+tam_min+","+tam_max+"&"


    def getData(self, local):

        counter = 1
        while True:      
            url = "https://brasilbrokers.com.br/busca/?"+"localizacao="+local+"&"+self.before+self.after+"pagina="+str(counter)
            

            agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
            r = requests.get(url, headers=agent)
            soup = BeautifulSoup(r.text, 'lxml')    

            if "Ops" in str(soup.select(".ajaxBlock span")):
                break
            else:
                for i in range(1,30):
                    preco = self.data_cleaner(str(soup.select(".ajaxBlock .resultItem:nth-child("+str(i)+") .valor")).replace(" ",""))
                    area = self.data_cleaner(str(soup.select(".ajaxBlock .resultItem:nth-child("+str(i)+") .area .numero span")).replace(" ",""))
                    n_quarto= self.data_cleaner(str(soup.select(".ajaxBlock .resultItem:nth-child("+str(i)+") .quarto .numero")).replace(" ",""))
                    n_vaga = self.data_cleaner(str(soup.select(".ajaxBlock .resultItem:nth-child("+str(i)+") .vaga .numero")).replace(" ",""))
                    n_banheiro = self.data_cleaner(str(soup.select(".ajaxBlock .resultItem:nth-child("+str(i)+") .banheiro .numero")).replace(" ",""))
                    descricao = self.data_cleaner(str(soup.select(".ajaxBlock .resultItem:nth-child("+str(i)+") .descricao")))
                    titulo = self.data_cleaner(str(soup.select(".ajaxBlock .resultItem:nth-child("+str(i)+") .headerInfo h2")))
                    self.table.append([preco.replace("\n",""),area.replace("\n",""),n_quarto.replace("\n",""),n_vaga.replace("\n",""),n_banheiro.replace("\n",""),descricao,titulo])
                print(f"\nDados da página {counter} de {local[-2]+local[-1]} coletados")
                counter += 1                
                
        self.create_csv(local)
        

    def create_csv(self, local):
        if "rj" in local:
            with open('imoveis_BrasilBrokers_RJ.csv', 'w', newline='', encoding='utf-8') as csvfile:
                file_csv = csv.writer(csvfile)
                for i in self.table:
                    file_csv.writerow(i)
        elif "sp" in local:
            with open('imoveis_BrasilBrokers_SP.csv', 'w', newline='', encoding='utf-8') as csvfile:
                file_csv = csv.writer(csvfile)
                for i in self.table:
                    file_csv.writerow(i)
    def data_cleaner(self, data):
        data_cleaned = ""
        check1 = False
        check2 = False
        check3 = False

        for i in data:
            if i == ">":
                check1 = True
            if i == "<" and check1 == True:
                check2 = True
            
            if check1 == True and check2 == False:
                if i.isalnum() == True:
                    check3 = True
                if check3 == True: 
                    data_cleaned = data_cleaned+i
        return (data_cleaned)
