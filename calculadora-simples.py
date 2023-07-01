# importando o tkinter
from tkinter import *

todos_valores = ''
# criando o a lógica de calculos
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    #Passando valor para tela
    valor_texto.set(todos_valores)
# função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    print(resultado)
    valor_texto.set(str(resultado))

# função limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#  cores
cor1 = '#050505' # preto
cor2 = '#fc0303' # vermelho
cor3 = '#1f7af0' # azul
cor4 = '#29912c' # verde

# criando o painel
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor2)

# Dividindo o painel e definindo
tela1 = Frame(janela,width=235,height=50, bg= cor1)
tela1.grid(row=0, column=0)

tela2 = Frame(janela,width=235,height=268)
tela2.grid(row=1,column=0)

# criando label
valor_texto = StringVar()
app_label = Label(tela1,textvariable=valor_texto,width=16,height=2,padx=7,relief=FLAT,anchor="e",justify= RIGHT,font=('Ivy 18'),bg=cor1,fg=cor2)
app_label.place(x=0,y=0)

# Criando os botões
# linha1
b_1 = Button(tela2,text="C",width=11, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:limpar_tela())
b_1.place(x=0,y=0)

b_2 = Button(tela2,text="%",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('%'))
b_2.place(x=120,y=0)

b_3 = Button(tela2,text="/",width=5, height=2,bg=cor4,fg=cor1,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('/'))
b_3.place(x=177,y=0)
# linha2
b_4 = Button(tela2,text="7",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('7'))
b_4.place(x=0,y=52)

b_5 = Button(tela2,text="8",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('8'))
b_5.place(x=59,y=52)

b_6 = Button(tela2,text="9",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('9'))
b_6.place(x=118,y=52)

b_7 = Button(tela2,text="*",width=5, height=2,bg=cor4,fg=cor1,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('*'))
b_7.place(x=177,y=52)
# linha3
b_8 = Button(tela2,text="4",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('4'))
b_8.place(x=0,y=104)

b_9 = Button(tela2,text="5",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('5'))
b_9.place(x=59,y=104)

b_10 = Button(tela2,text="6",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('6'))
b_10.place(x=118,y=104)

b_11 = Button(tela2,text="-",width=5, height=2,bg=cor4,fg=cor1,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('-'))
b_11.place(x=177,y=104)
# linha 4
b_12 = Button(tela2,text="1",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('1'))
b_12.place(x=0,y=156)

b_13 = Button(tela2,text="2",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('2'))
b_13.place(x=59,y=156)

b_14 = Button(tela2,text="3",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('3'))
b_14.place(x=118,y=156)

b_15 = Button(tela2,text="+",width=5, height=2,bg=cor4,fg=cor1,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('+'))
b_15.place(x=177,y=156)
# linha 5
b_16 = Button(tela2,text="0",width=11, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('0'))
b_16.place(x=0,y=208)

b_17 = Button(tela2,text=".",width=5, height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('.'))
b_17.place(x=120,y=208)

b_18 = Button(tela2,text="=",width=5, height=2,bg=cor4,fg=cor1,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:calcular())
b_18.place(x=177,y=208)

janela.mainloop()
