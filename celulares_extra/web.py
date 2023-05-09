from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from connect import con, cursor

class Web:
    def __init__(self, marca):
        self.marca = marca
        self.site = f'https://www.kabum.com.br/computadores/notebooks/notebook-{self.marca}'
        self.map = {
            "nome":{
                'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[@nome@]/a/div/button/div/h2/span'
            },
            "preco":{
               'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[@preco@]/a/div/div[1]/span[2]'
           }
       }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.criar_tabela()
        self.abrir_site(self.marca)

    def abrir_site(self, marca):
        self.driver.get(self.site)
        sleep(5)
        for i in range(1,11):
            descricao_p = self.driver.find_element(By.XPATH, self.map['nome']['xpath'].replace('@nome@',f'{i}')).text
            preco_p = self.driver.find_element(By.XPATH, self.map['preco']['xpath'].replace('@preco@', f'{i}')).text
            print(descricao_p, preco_p)
            inserir_note(marca, descricao_p, preco_p)

    def criar_tabela(self):
        cursor.execute(
            f"SELECT * FROM information_schema.tables WHERE table_name = '{self.marca}'")
        table_exists = cursor.fetchone()

        if table_exists:
            cursor.execute(f"DROP TABLE IF EXISTS {self.marca}")

        cursor.execute(
            f"""CREATE TABLE {self.marca} (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                                            descricao VARCHAR(255),
                                            preco VARCHAR(255)
                                            )""")
        con.commit()

def inserir_note(marca, id_prod, descricao, preco):
    inserir_note = f"""INSERT INTO {marca}(id, descricao, preco)
        values
    ({id_prod}, {descricao}, {preco})"""

    cursor = con.cursor()
    cursor.execute(inserir_note)
    con.commit()


y = Web('acer')