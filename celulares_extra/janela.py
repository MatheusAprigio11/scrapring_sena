from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from read import listar_sorteio
from connect import con, cursor
from web import Web
from marcas_comb import marcas_digitadas

janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.comboBox()
        self.inputs()
        self.lista_frame2()
        janela.mainloop()

    def tela(self):
        self.janela.title('NOTEBOOKS')
        self.janela.geometry('800x600')
        self.janela.configure(background='#858487')
        self.janela.resizable(FALSE, FALSE)
        self.janela.maxsize(width=800, height=550)

    def frames(self):
        self.frame_0 = Frame(self.janela, bg='black', highlightthickness=0.5, highlightbackground='white')
        self.frame_0.place(relx=0.03, rely=0.08, relwidth=0.94, relheight=0.13)

        self.frame_1 = Frame(self.janela, bg='black', highlightthickness=0.5, highlightbackground='white')
        self.frame_1.place(relx=0.03, rely=0.30, relwidth=0.94, relheight=0.35)


    def botoes(self):
        self.btLimpar = Button(self.frame_0, text='Limpar', bg='red', command=self.clear)
        self.btLimpar.place(relx=0.67, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btRead = Button(self.frame_0, text='Apresentar', bg='red', command=self.ler_modelo)
        self.btRead.place(relx=0.77, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btSearch = Button(self.frame_0, text='Buscar', bg='red', command=self.buscar_note)
        self.btSearch.place(relx=0.47, rely=0.25, relwidth=0.10, relheight=0.50)

    def comboBox(self):
        self.lb_marcas = Label(self.frame_0, text='Marcas', background='red')
        self.lb_marcas.pack()
        self.cb_marcas = ttk.Combobox(self.frame_0, values=marcas_digitadas)
        self.cb_marcas.pack()
        self.cb_marcas.place(relx=0.88, rely=0.30, relwidth=0.1, relheight=0.4)
        self.lb_marcas.place(relx=0.88, rely=0.02, relwidth=0.1, relheight=0.4)

    def inputs(self):
        self.lb_inpID = Label(self.frame_0, text='ID', background='red')
        self.lb_inpID.place(relx=0.34, rely = 0.02, relwidth=0.08, relheight=0.28)
        self.inpID = Entry(self.frame_0)
        self.inpID.place(relx=0.34, rely=0.25, relwidth=0.080, relheight=0.5)

    def lista_frame2(self):
        self.listaNot = ttk.Treeview(self.frame_1, height=3, columns=('col0',
                                                                      'col1',
                                                                      'col2',
                                                                      'col3'
                                                                      ))

        self.listaNot.heading('#0', text='')
        self.listaNot.heading('#1', text='noteID')
        self.listaNot.heading('#2', text='Descricao')
        self.listaNot.heading('#3', text='Valor')

        self.listaNot.column('#0', width=0)
        self.listaNot.column('#1', width=50)
        self.listaNot.column('#2', width=500)
        self.listaNot.column('#3', width=150)

        self.listaNot.place(relx=0.025, rely=0.080, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_1, orient='vertical')
        self.listaNot.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.98, rely=0.10, relwidth=0.02, relheight=0.85)

    def clear(self):
        self.listaNot.delete(*self.listaNot.get_children())

    def ler_modelo(self):
        self.clear()
        marca = self.cb_marcas.get().lower()
        consulta_sql = f"SHOW TABLES LIKE '{marca}'"
        cursor.execute(consulta_sql)
        existe_tabela = cursor.fetchone() is not None

        if existe_tabela:
            marcas = self.listar_tabela(marca)
            for modelo in marcas:
                self.listaNot.insert("", "end", values=modelo)
        else:
            Web(marca)

    def listar_tabela(self, marca):
        sql = f'SELECT * from {marca}'
        cursor.execute(sql)
        linhas = cursor.fetchall()
        return linhas

    def buscar_note(self):
        noteb = self.inpID.get()
        marca = self.cb_marcas.get().lower()
        print(noteb, '     ', marca)
        sql = f"SELECT * from {marca} WHERE noteID = {noteb};"
        cursor.execute(sql)
        linhas = cursor.fetchall()
        self.clear()
        self.listaNot.insert("", "end", values=linhas[0])


janelaapp = Aplicacao()
