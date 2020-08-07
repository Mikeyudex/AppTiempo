from tkinter import Tk, Entry, Button, Label
import requests

def mostrar_respuestas(clima):
    try:

        nombre_ciudad = clima['name']
        desc = clima['weather'][0]['description']
        tempe = clima['main']['temp']

        ciudad['text'] = nombre_ciudad
        temperatura['text'] = str(int(tempe)) + "º C"
        descripcion['text'] = desc
    except:
        ciudad['text'] = "Nombre Invalido"

def clima_JSON(ciudad):
    try:
        API_key = "65f7e16822c83cae98fb14c41a7109c6"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"appid" : API_key, "q": ciudad, "units": "metric", "lang": "es"}
        response = requests.get(URL, params=parametros)
        clima = response.json()
        mostrar_respuestas(clima)
    except:
        print("error")


   
ventana = Tk()
ventana.geometry("350x550")
ventana.title("App del Tiempo")


texto_ciudad = Entry(ventana, font = ("Verdana", 20, "normal"), justify = "center")
texto_ciudad.focus()
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text = "Obtener Clima", width = 20, height = 3, font = ("Verdana", 15, "normal"), command = lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(ventana, font = ("Verdana", 20, "normal"))
ciudad.pack(padx = 20, pady =20)

temperatura = Label(ventana, font = ("Verdana", 50, "normal"))
temperatura.pack(padx = 10, pady =10)

descripcion = Label(ventana, font = ("Verdana", 20, "normal"))
descripcion.pack(padx = 30, pady =30)



ventana.mainloop()
