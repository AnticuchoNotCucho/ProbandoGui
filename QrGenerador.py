import qrcode  # pip install qrcode
import os
import tkinter as tk
import time

#Crear ventana de tkinter
window = tk.Tk()
window.title("QR")
window.geometry('800x800')
window.resizable(False, False)


# valores vacios
img = tk.PhotoImage(file="")
text = ""


# definir el texto que se va a mostrar en el QR
def generarQR(texto):
    qrcode.make(texto).resize((500, 500)).save("QR.png")
    print("QR generado con exito")
    
def valorQR():
    generarQR(entry.get())
    img = tk.PhotoImage(file="QR.png")
    imageLabel.configure(image=img)
    imageLabel.image = img
    
def showtext():
    texto2.config(text="Texto ingresado a QR: " +entry.get())


# funcion para agrupar funciones y ejecutarlas e un solo comando
def all_functions():
    print(entry.get()), 
    valorQR(),
    showtext()


#inicio de valores vacios
img = tk.PhotoImage(file="")
text = ""

#generacion de QR


#parametros de objetos tkinter
frame = tk.Frame(height=500, width=500)

imageLabel = tk.Label(window, image=img,height=500, width=800)

entry = tk.Entry(window, width=50)

texto = tk.Label(window, text="Ingrese el texto que desea convertir a QR", font=("Arial", 12), fg="#A65E2E")

texto2 = tk.Label(window, text="Esperando texto", font=("Arial", 12))

Generate = tk.Button(window, text="Generar QR", command=all_functions, width=40, height=2,background="#869B74", foreground="#FFFFFF")

showQR =tk.Button(window, text="Guardar QR", command=lambda: os.system("QR.png") , width=40, height=2, background="#A65E2E", foreground="#FFFFFF")

close = tk.Button(window, text="Cerrar", command=window.destroy,width=40, height=2, background="#F4F1EA", foreground="black")

imageLabel.pack()
texto.pack()
entry.pack()
texto2.pack()
Generate.pack()
showQR.pack()
close.pack()
window.mainloop()

time.sleep(2)
os.remove("QR.png")
