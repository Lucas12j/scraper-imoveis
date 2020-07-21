# -*- coding: utf-8 -*-

import math
import requests
from bs4 import BeautifulSoup
import csv
import re

class GetDataOlx(object):
    
    def __init__(self, tipo, tipo_imovel, n_vagas, n_quartos, n_banheiros, area_min, area_max):
        self.table = [["PREÇO","ÁREA", "DESCRIÇÃO","ENDEREÇO","N° QUARTOS","N° VAGAS","CONCOMÍNIO","N° BANHEIROS REFERÊNTE A ESCOLHA DO USUARIO"]]
        self.after = ""
        self.before = ""
       
        area_res = {0:0,30:1,60:2,90:3,120:4,150:5,180:6,200:7,250:8,300:9,400:10,500:11,501:12}
        area_com = {0:0,50:3,100:8,150:10,200:12,300:14,400:15,500:16,800:17,1000:18,1500:19,2000:20,2500:21,3000:22,3001:23}
        list_area_min = []
        list_area_max = []

    
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
                if tipo == 1:
                    self.before = "comercio-e-industria/compra/"
                elif tipo ==2:
                    self.before = "comercio-e-industria/aluguel/"
            if tipo_imovel == 4:
                if tipo == 1:
                    self.before = "comercio-e-industria/compra/"
                elif tipo ==2:
                    self.before = "comercio-e-industria/aluguel/" 
                self.after = self.after+"&q=sala-comercial" 
            if tipo_imovel == 5:
                if tipo == 1:
                    self.before = "terrenos/compra/" 
                elif tipo ==2:
                    self.before = "terrenos/aluguel/"

            if tipo_imovel == 6:
                self.after = self.after+"&q=casas-de-condominio" 
            if tipo_imovel == 7:
                self.after = self.after+"&q=cobertura" 
            
        if n_vagas != "":
            self.after = self.after+"&gsp="+n_vagas
        if n_quartos != "":
            if n_quartos != "4":
                if n_quartos != "1":
                    self.before = self.before+n_quartos+"-quartos/"
                else:
                    self.before = self.before+n_quartos+"-quarto/"
            else:
                self.after = self.after+"&ros="+n_quartos
        if n_banheiros != "":
            if n_banheiros != "4":
                self.after = self.after+"&bae="+n_banheiros+"&bas="+n_banheiros
            else:
                self.after = self.after+"&bas="+n_quartos

        if area_min != "":
            if tipo_imovel != 3 and tipo_imovel != 4:
                for i in area_res:
                    list_area_min.append(math.fabs(int(area_min)-i))
                self.after =self.after+"&ss="+str(list(area_res.values())[list_area_min.index(min(list_area_min))])
            else:
                for i in area_com:
                    list_area_min.append(math.fabs(int(area_min)-i))
                self.after =self.after+"&ss="+str(list(area_com.values())[list_area_min.index(min(list_area_min))])
        if area_max != "":
            if tipo_imovel != 3 and tipo_imovel != 4:
                for i in area_res:
                    list_area_max.append(math.fabs(int(area_max)-i))
                self.after =self.after+"&se="+str(list(area_res.values())[list_area_max.index(min(list_area_max))])
            else:
                for i in area_com:
                    list_area_max.append(math.fabs(int(area_max)-i))
                self.after =self.after+"&se="+str(list(area_com.values())[list_area_max.index(min(list_area_max))])

    def getData(self, local, uf):
        aux = 1
        while True:
            url = "https://"+uf+".olx.com.br/"+local+"/imoveis/"+self.before+"?o="+str(aux)+self.after
            agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
            r = requests.get(url, headers=agent)
            soup = BeautifulSoup(r.text, 'lxml')   
            if "Ops!" in str(soup.select(".grqrOI")):
                break
            for idx in range(1,58):
                bedroom = ""
                area = ""
                garage = ""
                cond = ""
                if soup.select(".sc-1fcmfeb-2:nth-child("+str(idx)+") [data-lurker-detail]") != []:
                    price = self.cleaner_atr(soup.select(".sc-1fcmfeb-2:nth-child("+str(idx)+") .jqSHIm"), False)
                    description = self.cleaner_atr(soup.select(".sc-1fcmfeb-2:nth-child("+str(idx)+") .deEIZJ"), False)
                    address = self.cleaner_atr(soup.select(".sc-1fcmfeb-2:nth-child("+str(idx)+") .hdwqVC"), False)
                    atr = self.cleaner_atr(soup.select(".sc-1fcmfeb-2:nth-child("+str(idx)+") .jDoirm"), True)
                    for i in atr:
                        if "quarto" in i:
                            bedroom = int(re.compile('([0-9]+)').findall(i)[0])
                        if "m²" in i:
                            area = int(re.compile('([0-9]+)').findall(i)[0])
                        if "vaga" in i:
                            garage = int(re.compile('([0-9]+)').findall(i)[0])
                        if "Condo" in i:
                            cond = i.replace("Condomínio: ","")
                    self.table.append([price,area,description,address,bedroom,garage,cond])
            print(f"\nDados da página {aux} de {uf} coletados")
            aux+=1
        self.create_csv(local) 

    def cleaner_atr(self, atr, atr_verify):
        data_cleaned = ""
        check1 = False
        check2 = False
        for i in str(atr):
            if i == ">":
                check1 = True
            if i == "<" and check1 == True:
                check2 = True
            if check1 == True and check2 == False:
                data_cleaned = data_cleaned+i
        if atr_verify == True: 
            atr_cleaned = data_cleaned.replace(">","").split("|")
        else:
            atr_cleaned = data_cleaned.replace(">","")
        return atr_cleaned

            
    def create_csv(self, local):
        if "rio-de-janeiro" in local:
            with open('imoveis_olx_RJ.csv', 'w', newline='', encoding='utf-8') as csvfile:
                file_csv = csv.writer(csvfile)
                for i in self.table:
                    file_csv.writerow(i)
     
        elif "sao-paulo" in local:
            with open('imoveis_olx_SP.csv', 'w', newline='', encoding='utf-8') as csvfile:
                file_csv = csv.writer(csvfile)
                for i in self.table:
                    file_csv.writerow(i)
