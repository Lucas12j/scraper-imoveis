# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import csv


class GetDataVivaReal (object):

    def __init__(self, tipo, tipo_imovel, n_vagas, n_quartos, n_banheiros, tam_min, tam_max):
        
        option = Options()
        option.headless = True

        #COLOQUE AQUI O DIRETÓRIO ONDE SE ENCONTRA O GECKODRIVER CASO NECESSÁRIO, ADICIONANDO O SEGUINTE COMANDO NOS PARÂMETROS: executable_path=r'<DIRETORIO>'
        self.driver = webdriver.Firefox(options = option) 
        


        self.lista = [["PREÇO","TÍTULO","ENDEREÇO","ÁREA", "N° QUARTOS", "N° BANHEIRO","N° VAGAS", "CONDOMÍNIO"]]
        
        self.after = ""
        self.before = ""
        self.tipo = ""

        if tipo != "":
            if tipo == 1:
                self.tipo = "venda/"
            elif tipo == 2:
                self.tipo = "aluguel/"
        if tipo_imovel != "":
            if tipo_imovel == 1:
                self.before = "apartamento_residencial/"
            if tipo_imovel == 2:
                self.before = "casa_residencial/"
            if tipo_imovel == 3:
                self.before = "ponto-comercial_comercial/"
            if tipo_imovel == 4:
                self.before = "sala_comercial/"
            if tipo_imovel == 5:
                self.before = "lote-terreno_comercial/"
            if tipo_imovel == 6:
                self.before = "condominio_residencial/"
            if tipo_imovel == 7:
                self.before = "cobertura_residencial/"
            
        if n_vagas != "":
            self.after = self.after+"&vagas="+n_vagas
        if n_quartos != "":
            self.after = self.after+"&quartos="+n_quartos
        if n_banheiros != "":
            self.after = self.after+"&banheiros="+n_banheiros
        if tam_max != "":
            self.after=self.after+"&area-ate="+tam_max
        if tam_min != "":
            self.after=self.after+"&area-desde="+tam_min
        

    def getData(self, local):      
        page = 1
        url = "https://www.vivareal.com.br/"+self.tipo+local+self.before+"#onde=BR-Rio_de_Janeiro-NULL-Rio_de_Janeiro"+self.after
        
        self.driver.get(url)
        index_prox_pag = 1
        while True:
            try:
                html = self.driver.find_element_by_css_selector(".pagination__wrapper li:nth-child("+str(index_prox_pag)+") [title]").get_attribute('outerHTML')
                if "Próxima página" in html:
                    break
                index_prox_pag +=1
            except:
                break
        try:
            while True:
                time.sleep(4)
                for i in range(0,36):
                    title = self.cleaner(self.driver.find_element_by_css_selector(".results-list div .js-card-selector [data-index="+"\""+str(i)+"\""+"] .js-card-title").get_attribute('outerHTML'))
                    address = self.cleaner(self.driver.find_element_by_css_selector(".results-list div .js-card-selector [data-index="+"\""+str(i)+"\""+"] .js-property-card-address").get_attribute('outerHTML'))
                    area = self.cleaner(self.driver.find_element_by_css_selector(".results-list div .js-card-selector [data-index="+"\""+str(i)+"\""+"] .js-property-card-detail-area").get_attribute('outerHTML'))
                    bedrooms = self.cleaner(self.driver.find_element_by_css_selector(".results-list div .js-card-selector [data-index="+"\""+str(i)+"\""+"] .js-property-detail-rooms span").get_attribute('outerHTML'))
                    bathrooms = self.cleaner(self.driver.find_element_by_css_selector(".results-list div .js-card-selector [data-index="+"\""+str(i)+"\""+"] .js-property-detail-bathroom span").get_attribute('outerHTML'))
                    garages = self.cleaner(self.driver.find_element_by_css_selector(".results-list div .js-card-selector [data-index="+"\""+str(i)+"\""+"] .js-property-detail-garages span").get_attribute('outerHTML'))
                    price = self.cleaner(self.driver.find_element_by_css_selector(".results-list div .js-card-selector [data-index="+"\""+str(i)+"\""+"] .js-property-card__price-small").get_attribute('outerHTML'))
                    try:
                        condo = self.cleaner(self.driver.find_element_by_css_selector(".results-list div .js-card-selector [data-index="+"\""+str(i)+"\""+"] .js-condo-price").get_attribute('outerHTML')) 
                    except:
                        condo = "--"
                    self.lista.append([price.replace(" ","") ,title,address,area.replace(" ",""),bedrooms.replace(" ",""),bathrooms.replace(" ",""),garages.replace(" ",""),  condo.replace(" ","")])   
                self.driver.find_element_by_css_selector('.pagination__wrapper li:nth-child('+str(index_prox_pag)+') [data-page]').click()
                print(f"\nDados da página {page} de {local[0]+local[1]} coletados")
                
                page += 1 
        except: 
            self.create_csv(local)                                                                              
        
        finally:
            self.driver.quit()
            
    
    def cleaner(self, data):
        data_cleaned = ""
        check1 = False
        check2 = False
        data = data.replace("<br/>","")
        data = data.replace("\n","")
        for i in data:
            if i == ">":
                check1 = True
            if i == "<" and check1 == True:
                check2 = True
            if check1 == True and check2 == False:
                data_cleaned = data_cleaned+i
        return (data_cleaned.replace(">",""))

    def create_csv(self, local):
        if "rj" in local:
            with open('imoveis_VivaReal_RJ.csv', 'w', newline='', encoding='utf-8') as csvfile:
                file_csv = csv.writer(csvfile)
                for i in self.lista:
                    file_csv.writerow(i)
        elif "sp" in local:
            with open('imoveis_VivaReal_SP.csv', 'w', newline='', encoding='utf-8') as csvfile:
                file_csv = csv.writer(csvfile)
                for i in self.lista:
                    file_csv.writerow(i)




            
       

            

