# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:26:59 2020

@author: Manuela Molina O. (Batikitty)
"""
import pandas as pd
from selenium import webdriver
import requests

"Leer el documento"
doc = pd.read_excel('BOOKS.xlsx')

"""
A continuación se filtra según el tema de interés a descargar y se muestra la 
lista y cantidad de libros que descargaré.  
"""
tema = doc[doc['EnglishPackageName'] == 'ReligionandPhilosophy']
print(tema)

"Ahora se inicia el ciclo que hará todo el trabajo:"
for index, i in tema.iterrows():
    """
    Gracias a Selenium se puede interactuar con el navegador, en este caso 
    Chrome así que se arrancán los drivers propios de éste y luego abrimos la 
    URL de la columna OpenURL
    """
    driver = webdriver.Chrome(executable_path='/Users/manue/Desktop/Carpetita/chromedriver')
    driver.get(doc.OpenURL[index])
    """
    En las páginas aparece un botón de descarga el cual identificamos por medio
    del Xpath de éstos. Lo que se pudo notar es que no todas las URL llevaban a
    páginas con los mismos Xpath así que toca que el bucle intente buscar uno y si
    no lo encuentra busca el otro. Una vez encuentra el Xpath de la página
    obtiene de él el href y por medio de ese href se realiza la descarga del pdf
    poniendo el nombre del libro de la columna BookTitle. Si definitivamente no
    encontró Xpath, nos dará el nombre del libro en cuestión ya sea para revisar
    la URL de ese libro e incluir el Xpath de ésta o simplemente descargarlo manualmente.
    Tras todo esto, cierra la ventana del navegador que abrío y vuelve a empezar con 
    otra fila.
    """
    xpath1 = '//*[@id="main-content"]/article[1]/div/div/div[2]/div/div/a'
    xpath2 = '//*[@id="main-content"]/article[1]/div/div/div[2]/div[1]/a'
    try:
        button = driver.find_element_by_xpath(xpath1)
        url = button.get_attribute("href")
        r = requests.get(url)
        open('/Users/manue/Desktop/Carpetita/ReligionandPhilosophy/'+doc.BookTitle[index]+'.pdf', 'wb').write(r.content)
    except: 
        try:
           button = driver.find_element_by_xpath(xpath2)
           url = button.get_attribute("href")
           r = requests.get(url)
           open('/Users/manue/Desktop/Carpetita/ReligionandPhilosophy/'+doc.BookTitle[index]+'.pdf', 'wb').write(r.content)
        except:
            print (doc.BookTitle[index])
    finally:
        driver.quit()
     
     
