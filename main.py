# Importando tkinter
from tkinter import *
from tkinter import ttk

# Cores
cor1 = "#050505"  # black/preta
cor2 = "#fcfcfc"  # white/branca
cor3 = "#086682"  # azul carregado
cor4 = "#68787d"  # cinza
cor5 = "#d44106"  # orange/laranja

janela = Tk()
janela.title('Calculadora')
janela.geometry("235x310")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)

# Variável todos valores
todos_valores = ''

# Função para entrada de valores
def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

# Função para calcular o resultado
def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except:
        valor_texto.set("Erro")
        todos_valores = ""

# Função para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Criando Label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief="flat", anchor="e", justify="right", font=('ivy 18'))
app_label.place(x=0, y=0)

# Criando botões
b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=limpar_tela)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('%'))
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('/'))
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('9'))
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('8'))
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('7'))
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('*'))
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, text="6", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('6'))
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, text="5", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('5'))
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, text="4", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('4'))
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, text="-", width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('-'))
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, text="3", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('3'))
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, text="2", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('2'))
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, text="1", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('1'))
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, text="+", width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('+'))
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, text="0", width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('0'))
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, text=".", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('.'))
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=calcular)
b_18.place(x=177, y=208)

janela.mainloop()
