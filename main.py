from tkinter import Tk, ttk
from tkinter import *

# importando bibliotecas externas ----------------------------------------------------------------

from PIL import Image, ImageTk, ImageOps, ImageDraw

import requests 
import json
import string

# cores ----------------------------------------------------------------

cor0 = "#FFFFFF"
cor1 = "#000000"
cor2 = "#800100"

# configurando a janela ----------------------------------------------------------------

janela = Tk()
janela.geometry('300x320') #largura e altura
janela.title('Conversor') 
janela.configure(bg=cor0) #cor do fundo da janela 
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")

# Divisão da janela ----------------------------------------------------------------

frame_cima = Frame(janela, width=300, height=60, padx=0, pady=0, bg=cor1, relief='flat')
frame_cima.grid(row=0,column=0, columnspan=2)

frame_baixo = Frame(janela, width=300, height=260, padx=0, pady=5, bg=cor0, relief='flat')
frame_baixo.grid(row=1,column=0, sticky=NSEW)

# Função converter ----------------------------------------------------------------

def converter():
    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_entrado = valor.get()

    response = requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de))
    dados = json.loads(response.text)
    cambio = dados['rates'][moeda_para]

    resultado = float(valor_entrado) * float(cambio)

    if moeda_para == 'USD':
        simbolo = '$'
    elif moeda_para == 'EUR':
        simbolo = '£'
    elif moeda_para == 'INR':
        simbolo = '₹'
    elif moeda_para == 'AOA':
        simbolo = 'Kz'
    elif moeda_para == 'AED':
        simbolo = 'د. إ'  
    elif moeda_para == 'AFN':
        simbolo = '؋'    
    elif moeda_para == 'ALL':
        simbolo = 'L'    
    elif moeda_para == 'AMD':
        simbolo = '֏'    
    elif moeda_para == 'ANG':
        simbolo = 'ƒ'    
    elif moeda_para == 'ARS':
        simbolo = '$'    
    elif moeda_para == 'AUD':
        simbolo = 'A$'    
    elif moeda_para == 'AWG':
        simbolo = 'ƒ'    
    elif moeda_para == 'AZN':
        simbolo = '₼'          
    elif moeda_para == 'BAM':
        simbolo = 'KM'    
    elif moeda_para == 'BBD':
        simbolo = 'Bds$'    
    elif moeda_para == 'BDT':
        simbolo = '৳'    
    elif moeda_para == 'BGN':
        simbolo = 'лв'    
    elif moeda_para == 'BHD':
        simbolo = 'د. ب'    
    elif moeda_para == 'BIF':
        simbolo = 'FBu'    
    elif moeda_para == 'BSD':
        simbolo = '$'  
    elif moeda_para == 'BTN':
        simbolo = 'Nu'                 
    elif moeda_para == 'BWP':
        simbolo = 'P'                 
    elif moeda_para == 'BYN':
        simbolo = 'Br'                 
    elif moeda_para == 'BZD':
        simbolo = 'BZ$'                 
    elif moeda_para == 'CAD':
        simbolo = 'C$'                 
    elif moeda_para == 'CDF':
        simbolo = 'FC'                 
    elif moeda_para == 'CHF':
        simbolo = 'SFr'                 
    elif moeda_para == 'CLP':
        simbolo = '$'                                                                     
    elif moeda_para == 'CNY':
        simbolo = '元/¥' 
    elif moeda_para == 'CRC':
        simbolo = '₡'         
    elif moeda_para == 'CUP':
        simbolo = '₱' 
    elif moeda_para == 'CVE':
        simbolo = 'Esc' 
    elif moeda_para == 'CZK':
        simbolo = 'Kč' 
    elif moeda_para == 'DJF':
        simbolo = 'Fdj'         
    elif moeda_para == 'DKK':
        simbolo = 'Kr' 
    elif moeda_para == 'DOP':
        simbolo = 'RD$' 
    elif moeda_para == 'EGP':
        simbolo = '£' 
    elif moeda_para == 'ERN':
        simbolo = 'Nfk' 
    elif moeda_para == 'ETB':
        simbolo = 'Br' 
    elif moeda_para == 'FJD':
        simbolo = 'FJ $' 
    elif moeda_para == 'FKP':
        simbolo = '£' 
    elif moeda_para == 'FOK':
        simbolo = 'FK £' 
    elif moeda_para == 'GBP':
        simbolo = '£' 
    elif moeda_para == 'GEL':
        simbolo = '₾'         
    elif moeda_para == 'GGP':
        simbolo = '£' 
    elif moeda_para == 'GHS':
        simbolo = 'GH₵' 
    elif moeda_para == 'GIP':
        simbolo = '£' 
    elif moeda_para == 'GMD':
        simbolo = 'D' 
    elif moeda_para == 'GNF':
        simbolo = 'FG'         
    elif moeda_para == 'GTQ':
        simbolo = 'G$' 
    elif moeda_para == 'GYD':
        simbolo = 'G$' 
    elif moeda_para == 'HKD':
        simbolo = 'HK$' 
    elif moeda_para == 'HNL':
        simbolo = 'L'         
    elif moeda_para == 'HRK':
        simbolo = 'kn' 
    elif moeda_para == 'HTG':
        simbolo = 'G' 
    elif moeda_para == 'HUF':
        simbolo = 'Ft' 
    elif moeda_para == 'IDR':
        simbolo = 'Rp ' 
    elif moeda_para == 'ILS':
        simbolo = '₪' 
    elif moeda_para == 'IMP':
        simbolo = 'a$' 
    elif moeda_para == 'IQD':
        simbolo = 'ع. د' 
    elif moeda_para == 'IRR':
        simbolo = '﷼'  
    elif moeda_para == 'JEP':
        simbolo = '£' 
    elif moeda_para == 'JMD':
        simbolo = 'J$'         
    elif moeda_para == 'JOD':
        simbolo = 'د.ا' 
    elif moeda_para == 'JPY':
        simbolo = '¥' 
    elif moeda_para == 'KES':
        simbolo = 'KSh' 
    elif moeda_para == 'KGS':
        simbolo = 'лв' 
    elif moeda_para == 'KHR':
        simbolo = '៛'         
    elif moeda_para == 'KID':
        simbolo = 'C$' 
    elif moeda_para == 'ISK':
        simbolo = 'kr' 
    elif moeda_para == 'KMF':
        simbolo = 'CF' 
    elif moeda_para == 'KRW':
        simbolo = '₩' 
    elif moeda_para == 'KWD':
        simbolo = 'KD'         
    elif moeda_para == 'KYD':
        simbolo = 'CI$' 
    elif moeda_para == 'KZT':
        simbolo = '₸'         
    elif moeda_para == 'LAK':
        simbolo = '₭'
    elif moeda_para == 'LBP':
        simbolo = '£'
    elif moeda_para == 'LKR':
        simbolo = 'Rs'
    elif moeda_para == 'LRD':
        simbolo = 'LD$'         
    elif moeda_para == 'LSL':
        simbolo = 'G'
    elif moeda_para == 'LYD':
        simbolo = 'ل.د'
    elif moeda_para == 'MAD':
        simbolo = '.د.م'
    elif moeda_para == 'MDL':
        simbolo = 'L'         
    elif moeda_para == 'MGA':
        simbolo = 'Ar'
    elif moeda_para == 'MKD':
        simbolo = 'ден'
    elif moeda_para == 'MMK':
        simbolo = 'K'
    elif moeda_para == 'MNT':
        simbolo = '₮'         
    elif moeda_para == 'MOP':
        simbolo = 'MOP$'
    elif moeda_para == 'MRU':
        simbolo = 'UM'
    elif moeda_para == 'MUR':
        simbolo = 'Rs'
    elif moeda_para == 'MVR':
        simbolo = 'Rf'         
    elif moeda_para == 'MWK':
        simbolo = ''
    elif moeda_para == 'MXN':
        simbolo = '$'
    elif moeda_para == 'MZN':
        simbolo = 'MTn'
    elif moeda_para == 'NAD':
        simbolo = 'N$'         
    elif moeda_para == 'NGN':
        simbolo = '₦'
    elif moeda_para == 'NIO':
        simbolo = 'NIO'
    elif moeda_para == 'NOK':
        simbolo = 'KR'
    elif moeda_para == 'NPR':
        simbolo = '₨'
    elif moeda_para == 'NZD':
        simbolo = '$'
    elif moeda_para == 'OMR':
        simbolo = '﷼'
    elif moeda_para == 'PAB':
        simbolo = 'B/'
    elif moeda_para == 'PEN':
        simbolo = 'S/'
    elif moeda_para == 'PGK':
        simbolo = 'K'        
    elif moeda_para == 'PHP':
        simbolo = '₱'
    elif moeda_para == 'PKR':
        simbolo = '₨'
    elif moeda_para == 'PLN':
        simbolo = 'zł'
    elif moeda_para == 'PYG':
        simbolo = '₲'
    elif moeda_para == 'QAR':
        simbolo = '﷼'
    elif moeda_para == 'RON':
        simbolo = 'L'
    elif moeda_para == 'RSD':
        simbolo = 'Дин'
    elif moeda_para == 'RUB':
        simbolo = '₽'
    elif moeda_para == 'RWF':
        simbolo = 'R₣'
    elif moeda_para == 'SAR':
        simbolo = '﷼.'
    elif moeda_para == 'SBD':
        simbolo = 'SI$'
    elif moeda_para == 'SCR':
        simbolo = '₨'
    elif moeda_para == 'SDG':
        simbolo = 'ج. س'
    elif moeda_para == 'SEK':
        simbolo = 'kr'
    elif moeda_para == 'SGD':
        simbolo = 'S$'
    elif moeda_para == 'SHP':
        simbolo = 'SHP' 
    elif moeda_para == 'SLE':
        simbolo = 'PYG'
    elif moeda_para == 'SLL':
        simbolo = 'S /'
    elif moeda_para == 'SOS':
        simbolo = 'SOS'
    elif moeda_para == 'SRD':
        simbolo = '$'
    elif moeda_para == 'SSP':
        simbolo = 'SS£'
    elif moeda_para == 'STN':
        simbolo = 'Db'
    elif moeda_para == 'SYP':
        simbolo = '£'
    elif moeda_para == 'SZL':
        simbolo = 'L'
    elif moeda_para == 'THB':
        simbolo = '฿'
    elif moeda_para == 'TJS':
        simbolo = 'SM'
    elif moeda_para == 'TMT':
        simbolo = 'T'
    elif moeda_para == 'TND':
        simbolo = 'د. ت'
    elif moeda_para == 'TOP':
        simbolo = 'T$'
    elif moeda_para == 'TRY':
        simbolo = '₺'
    elif moeda_para == 'TTD':
        simbolo = 'TT$'
    elif moeda_para == 'TVD':
        simbolo = '$'
    elif moeda_para == 'TWD':
        simbolo = 'NT$'
    elif moeda_para == 'TZS':
        simbolo = 'TSh'
    elif moeda_para == 'UAH':
        simbolo = '₴'
    elif moeda_para == 'UGX':
        simbolo = 'USh'                
    elif moeda_para == 'UYU':
        simbolo = '$U' 
    elif moeda_para == 'UZS':
        simbolo = 'лв' 
    elif moeda_para == 'VES':
        simbolo = 'Bs' 
    elif moeda_para == 'VND':
        simbolo = '₫'
    elif moeda_para == 'VUV':
        simbolo = 'VT'
    elif moeda_para == 'WST':
        simbolo = 'WS$'                
    elif moeda_para == 'XAF':
        simbolo = 'FCFA'  
    elif moeda_para == 'XCD':
        simbolo = '$'  
    elif moeda_para == 'XDR':
        simbolo = 'SZR'  
    elif moeda_para == 'XOF':
        simbolo = 'CFA'
    elif moeda_para == 'XPF':
        simbolo = '₣'
    elif moeda_para == 'YER':
        simbolo = '﷼'        
    elif moeda_para == 'ZAR':
        simbolo = 'R' 
    elif moeda_para == 'ZMW':
        simbolo = 'ZK'         
    elif moeda_para == 'ZWL':
        simbolo = 'Z$'   
    else:
        simbolo = 'R$'
        
    moeda_equivalente = simbolo + "{:,.2f}".format(resultado)
    print(moeda_equivalente)

    app_resultado['text'] = moeda_equivalente

# Configuração para frame cima ----------------------------------------------------------------

icon = Image.open('imagem/icon.png')
icon = icon.resize((40, 40), Image.AFFINE) #antilias não funcionou aqui, averiguar posteriormente 
icon = ImageTk.PhotoImage(icon)

app_nome = Label(frame_cima, image=icon, compound=LEFT, text='Conversor de moeda ', height=5, pady=30, padx=13, relief='raised', anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_nome.place(x=0, y=0)    

# Configuração para frame baixo ----------------------------------------------------------------

app_resultado = Label(frame_baixo, text='', width=16, height=2, relief='solid', anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
app_resultado.place(x=50, y=10)  

moeda = ['AOA','BRL', 'EUR', 'INR', 'USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG','ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB','FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK','HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB','PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST','XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']

app_de = Label(frame_baixo, text='De', width=8, height=1, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
app_de.place(x=48, y=90) 
combo_de = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo_de.place(x=50, y=115) 
combo_de['values'] = (moeda)

app_para = Label(frame_baixo, text='Para', width=8, height=1, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
app_para.place(x=158, y=90) 
combo_para = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo_para.place(x=160, y=115) 
combo_para['values'] = (moeda)

valor = Entry(frame_baixo, width=22, justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
valor.place(x=50, y=155)

botao = Button(frame_baixo, command=converter, text='Converter ', width=19, padx=5, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'), relief='raised', overrelief=RIDGE)
botao.place(x=50, y=210)

janela.mainloop()