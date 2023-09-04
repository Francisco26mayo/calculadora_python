
import tkinter
ventana=tkinter.Tk()
ventana.geometry("+10+10")
ventana.title("calculadora")


ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1,weight=1)






def Sumar():
  try:
    valor1 = e_valor1.get()
    valor2 = e_valor2.get()
    Label_Resultado.grid( row=7, column=0,  columnspan=2 )

    if valor1=="" or valor2=="":
        Label_Resultado["text"]= "!Falta de valores para suma!"
        messagebox.showwarning("Error","Falta valores para suma")
    else:
        resultado=int(valor1)+int(valor2)
        Label_Resultado["text"]=resultado
  except:
    messagebox.showerror("Error en nivel 1","Error de valores no valido")





def resta():
  try:
    valor1 = e_valor1.get()
    valor2 = e_valor2.get()
    Label_Resultado.grid( row=7, column=0,  columnspan=2 )

    if valor1=="" or valor2=="":
        Label_Resultado["text"]= "!Falta de valores para suma!"
        messagebox.showwarning("Error","Falta valores para suma")
    else:
        resultado=int(valor1)-int(valor2)
        Label_Resultado["text"]=resultado
  except:
    messagebox.showerror("Error en nivel 2","Error de valores no valido")


   

def Division():
    valor1 = e_valor1.get()
    valor2 = e_valor2.get()
    Label_Resultado.grid( row=7, column=0,  columnspan=2 )

    if valor1=="" or valor2=="":
        Label_Resultado["text"]= "!Falta de valores para suma!"
        messagebox.showwarning("Error","Falta valores para suma")
    else:
        resultado=int(valor1)/int(valor2)
        Label_Resultado["text"]=resultado
  

def multiplicacion():

    valor1 = e_valor1.get()
    valor2 = e_valor2.get()
    Label_Resultado.grid( row=7, column=0,  columnspan=2 )

    if valor1=="" or valor2=="":
        Label_Resultado["text"]= "!Falta de valores para suma!"
        messagebox.showwarning("Error","Falta valores para suma")
    else:
        resultado=int(valor1)*int(valor2)
        Label_Resultado["text"]=resultado
 
   






ventana.rowconfigure(0, weight=0)
ventana.rowconfigure(1, weight=0)
ventana.rowconfigure(2, weight=0)
ventana.rowconfigure(3, weight=0)
ventana.rowconfigure(4, weight=0)
ventana.rowconfigure(5, weight=0)
ventana.rowconfigure(6, weight=0)



label_titulo = tkinter.Label(ventana, text="calculadora", font="arial 25")

label_valor1 = tkinter.Label(ventana, text=" valor 1", font="arial 12")
label_valor2 = tkinter.Label(ventana, text="valor 2 ", font="arial 12")

e_valor1= tkinter.Entry(ventana, font="arial 15")
e_valor2= tkinter.Entry(ventana,  font="arial 15")

button_suma = tkinter.Button(ventana,  text="suma", bg="black", fg="white", font="arial 20", width="18", command=Sumar)
button_resta = tkinter.Button(ventana,  text="resta", bg="green", fg="white", font="arial 20", width="18", command=resta)
button_multi = tkinter.Button(ventana,  text="multiplicacion", bg="red", fg="white", font="arial 20", width="18", command=multiplicacion)
button_Division = tkinter.Button(ventana,  text="Division", bg="blue", fg="white", font="arial 20", width="18", command=Division)



label_titulo.grid( row=0, column=0, columnspan=2, pady=5)
label_valor1.grid(row=1, column=0)
label_valor2.grid(row=2, column=0)


e_valor1.grid(row=1, column=1)
e_valor2.grid(row=2, column=1)

button_suma.grid(row=3, column=0 ,pady=5, columnspan=2)
button_resta.grid(row=4, column=0, pady=4, columnspan=2)
button_multi.grid(row=6, column=0, pady=4, columnspan=2)
button_Division.grid(row=5, column=0, pady=4, columnspan=2)

label_valor1.grid(row=5, column=0, pady=4, columnspan=2)
label_valor2.grid(row=5, column=0, pady=4, columnspan=2)

Label_Resultado=tkinter.Label(ventana)





ventana.mainloop() 