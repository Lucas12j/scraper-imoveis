import tkinter as tk
from library import get_data_zap, get_data_vivaReal, get_data_brasilBrokers, get_data_olx


class Graph_Int(object):


    def __init__(self):
        window = tk.Tk()
        window["bg"] = 'cyan'
        window.title("OLÁ")
        window.geometry("513x655+800+80")

        self.tipo = tk.IntVar()
        self.tipo_imovel = tk.IntVar()
        self.n_vaga = tk.StringVar()
        self.n_quarto = tk.StringVar()
        self.n_banheiro = tk.StringVar()

        welcome = tk.Label(window, text="SEJA BEM-VINDO",bg = "black", fg = "white", pady = 15)
        welcome.grid(row= 0, column = 0, columnspan = 4, sticky = "WE")

        l_tipo = tk.Label(window, text = "TIPO", width = 72)
        r_tipo1 = tk.Radiobutton(window, text = "VENDA", value = 1,variable = self.tipo)
        r_tipo2 = tk.Radiobutton(window, text = "ALUGUEL", value = 2,variable = self.tipo)
        l_tipo.grid(row= 1, column = 0, columnspan = 4, sticky = "WE", pady = 15)
        r_tipo1.grid(row = 2, column = 0, columnspan = 2)
        r_tipo2.grid(row = 2, column = 2, columnspan = 3)

        l_tipo_imovel = tk.Label(window, text = "TIPO DE IMÓVEL", width = 72)
        r_tipo_imovel1 = tk.Radiobutton(window, text = "APARTAMENTO", value = 1,variable = self.tipo_imovel)
        r_tipo_imovel2 = tk.Radiobutton(window, text = "CASA", value = 2, variable = self.tipo_imovel)
        r_tipo_imovel3 = tk.Radiobutton(window, text = "UNIDADES COMERCIAIS", value = 3, variable = self.tipo_imovel)
        r_tipo_imovel4 = tk.Radiobutton(window, text = "CONJUNTO/SALA COMERCIAL", value = 4,  variable = self.tipo_imovel)
        r_tipo_imovel5 = tk.Radiobutton(window, text = "TERRENOS/LOTES", value = 5,  variable = self.tipo_imovel)
        r_tipo_imovel6 = tk.Radiobutton(window, text = "CASAS DE CONDOMÍNIO", value = 6,  variable = self.tipo_imovel)
        r_tipo_imovel7 = tk.Radiobutton(window, text = "COBERTURAS", value = 7,  variable = self.tipo_imovel)
        l_tipo_imovel.grid(row= 3, column = 0, columnspan = 4, sticky = "WE", pady = 15)
        r_tipo_imovel1.grid(row = 4, column = 1, columnspan = 2, pady = 10)
        r_tipo_imovel2.grid(row = 5, column = 1, columnspan = 2)
        r_tipo_imovel3.grid(row = 4, column = 3,sticky = "W")
        r_tipo_imovel4.grid(row = 6, column = 0, pady = 10,sticky = "E")
        r_tipo_imovel5.grid(row = 6, column = 3,sticky = "W")
        r_tipo_imovel6.grid(row = 4, column = 0,sticky = "E")
        r_tipo_imovel7.grid(row = 6, column = 1, columnspan = 2)

        l_tamanho_imovel = tk.Label(window, text = "TAMANHO DO IMÓVEL", width = 72)
        l_area_min = tk.Label(window, text = "MIN", width = 10)
        l_area_max = tk.Label(window, text = "MAX", width = 10)
        self.text_area_min = tk.Entry(window, width = 10)
        self.text_area_max = tk.Entry(window, width = 10)
        l_tamanho_imovel.grid(row= 7, column = 0, columnspan = 4, sticky = "WE", pady = 15)
        l_area_min.grid(row= 8, column = 0)
        l_area_max.grid(row= 8, column = 2)
        self.text_area_min.grid(row  = 8, column = 1, columnspan = 1, sticky = "W")
        self.text_area_max.grid(row  = 8, column = 3, columnspan = 1)

        l_num_vaga = tk.Label(window, text = "NÚMERO DE VAGAS", width = 72)
        r_vaga_1 = tk.Checkbutton(window, text = "1", onvalue = "1",offvalue = "", variable = self.n_vaga)
        r_vaga_2 = tk.Checkbutton(window, text = "2", onvalue = "2",offvalue = "", variable = self.n_vaga)
        r_vaga_3 = tk.Checkbutton(window, text = "3", onvalue = "3", offvalue = "",variable = self.n_vaga)
        r_vaga_4 = tk.Checkbutton(window, text = "+4", onvalue = "4", offvalue = "",variable = self.n_vaga)
        l_num_vaga.grid(row= 9, column = 0, columnspan = 4, sticky = "WE", pady = 15)
        r_vaga_1.grid(row = 10, column = 0)
        r_vaga_2.grid(row = 10, column = 1)
        r_vaga_3.grid(row = 10, column = 2)
        r_vaga_4.grid(row = 10, column = 3)

        l_num_quarto= tk.Label(window, text = "NÚMERO DE QUARTOS", width = 72)
        r_quarto_1 = tk.Checkbutton(window, text = "1", onvalue = "1",offvalue = "", variable = self.n_quarto)
        r_quarto_2 = tk.Checkbutton(window, text = "2", onvalue = "2", offvalue = "",variable = self.n_quarto)
        r_quarto_3 = tk.Checkbutton(window, text = "3", onvalue = "3", offvalue = "",variable = self.n_quarto)
        r_quarto_4 = tk.Checkbutton(window, text = "+4", onvalue = "4",offvalue = "", variable = self.n_quarto)
        l_num_quarto.grid(row= 11, column = 0, columnspan = 4, sticky = "WE", pady = 15)
        r_quarto_1.grid(row = 12, column = 0)
        r_quarto_2.grid(row = 12, column = 1)
        r_quarto_3.grid(row = 12, column = 2)
        r_quarto_4.grid(row = 12, column = 3)

        l_num_banheiro = tk.Label(window, text = "NÚMERO DE BANHEIROS", width = 72)
        r_banheiro_1 = tk.Checkbutton(window, text = "1", onvalue = "1", offvalue = "",variable = self.n_banheiro)
        r_banheiro_2 = tk.Checkbutton(window, text = "2", onvalue = "2", offvalue = "",variable = self.n_banheiro)
        r_banheiro_3 = tk.Checkbutton(window, text = "3", onvalue = "3", offvalue = "",variable = self.n_banheiro)
        r_banheiro_4 = tk.Checkbutton(window, text = "+4", onvalue = "4", offvalue = "",variable = self.n_banheiro)
        l_num_banheiro.grid(row= 13, column = 0, columnspan = 4, sticky = "WE", pady = 15)
        r_banheiro_1.grid(row = 14, column = 0)
        r_banheiro_2.grid(row = 14, column = 1)
        r_banheiro_3.grid(row = 14, column = 2)
        r_banheiro_4.grid(row = 14, column = 3)

        button = tk.Button(window,  text = "INICIAR", command = self.send)
        button.grid(row = 15, column = 1, columnspan = 2, pady = 25, sticky = "WE")
        button["bg"] = "green"
        button["fg"] = "white"

        window.mainloop()


    def send(self):
	    
        '''print("\n\nPROCESSO NO SITE ZAP INICIADO\n\n")
        get_data_zap.GetDataZap(self.tipo.get(), self.tipo_imovel.get(), self.n_vaga.get(), self.n_quarto.get(),self.n_banheiro.get(), self.text_area_min.get(), self.text_area_max.get()).getData("rj+rio-de-janeiro/")  
        get_data_zap.GetDataZap(self.tipo.get(), self.tipo_imovel.get(), self.n_vaga.get(), self.n_quarto.get(),self.n_banheiro.get(), self.text_area_min.get(), self.text_area_max.get()).getData("sp+sao-paulo/")
        print("\n\nPROCESSO NO SITE ZAP FINALIZADO")'''


        
        print("\n\nPROCESSO NO SITE VIVAREAL INICIADO\n\n")
        get_data_vivaReal.GetDataVivaReal(self.tipo.get(), self.tipo_imovel.get(), self.n_vaga.get(), self.n_quarto.get(),self.n_banheiro.get(), self.text_area_min.get(), self.text_area_max.get()).getData("rj/rio-de-janeiro/")
        get_data_vivaReal.GetDataVivaReal(self.tipo.get(), self.tipo_imovel.get(), self.n_vaga.get(), self.n_quarto.get(),self.n_banheiro.get(), self.text_area_min.get(), self.text_area_max.get()).getData("sp/sao-paulo/")
        print("\n\nPROCESSO NO SITE VIVAREAL FINALIZADO")
        print("\n\nPROCESSO NO SITE BRASILBROKERS INICIADO\n\n")
        get_data_brasilBrokers.GetDataBrasilBrokers(self.tipo.get(), self.tipo_imovel.get(), self.n_vaga.get(), self.n_quarto.get(),self.n_banheiro.get(), self.text_area_min.get(), self.text_area_max.get()).getData("rio-de-janeiro|rj")
        get_data_brasilBrokers.GetDataBrasilBrokers(self.tipo.get(), self.tipo_imovel.get(), self.n_vaga.get(), self.n_quarto.get(),self.n_banheiro.get(), self.text_area_min.get(), self.text_area_max.get()).getData("sao-paulo|sp")
        print("\n\nPROCESSO NO SITE BRASILBROKERS FINALIZADO")
        print("\n\nPROCESSO NO SITE OLX INICIADO\n\n")
        get_data_olx.GetDataOlx(self.tipo.get(), self.tipo_imovel.get(), self.n_vaga.get(), self.n_quarto.get(),self.n_banheiro.get(), self.text_area_min.get(), self.text_area_max.get()).getData("rio-de-janeiro-e-regiao","rj")
        get_data_olx.GetDataOlx(self.tipo.get(), self.tipo_imovel.get(), self.n_vaga.get(), self.n_quarto.get(),self.n_banheiro.get(), self.text_area_min.get(), self.text_area_max.get()).getData("sao-paulo-e-regiao","sp")
        print("\n\nPROCESSO NO SITE OLX FINALIZADO")
        self.text_area_max.delete(0,tk.END)
        self.text_area_min.delete(0,tk.END)
        
