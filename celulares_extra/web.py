from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from connect import con, cursor
marcas_digitadas = []

class Web:
    def __init__(self, marca):
        self.marca = marca
        self.site = f'https://www.kabum.com.br/computadores/notebooks/notebook-{self.marca}'
        marcas_digitadas.append(marca)
        self.map = {
            "nome": {
                'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[%desc%]/a/div/button/div/h2/span'
            },
            "nums": {
                'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[@valor@]/a/div/div[1]/span[2]'
            }
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.criar_tabela()
        self.abrir_site()
    def abrir_site(self):
        self.driver.get(self.site)
        sleep(5)
        results = []
        for i in range(1, 11):
            legend = self.driver.find_element(By.XPATH, self.map['nome']['xpath'].replace('%desc%', f'{i}')).text

            valor = self.driver.find_element(By.XPATH, self.map['nums']['xpath'].replace('@valor@', f'{i}')).text
            results.append((legend, valor))

        query = f"INSERT INTO {self.marca} (legend, valor) VALUES (%s, %s)"

        cursor.executemany(query, results)
        con.commit()

    def criar_tabela(self):
        cursor.execute(
            f"SELECT * FROM information_schema.tables WHERE table_name = '{self.marca}'")
        table_exists = cursor.fetchone()

        if table_exists:
            cursor.execute(f"DROP TABLE IF EXISTS {self.marca}")

        cursor.execute(
            f"CREATE TABLE {self.marca} (noteID int NOT NULL AUTO_INCREMENT PRIMARY KEY, legend VARCHAR(255), valor VARCHAR(255));")
        con.commit()

    def deletar_tabela(self):
        sql = f"DELETE FROM {self.marca} WHERE noteID = '{id}';"
        cursor.execute(sql)
        cursor.fetchall()

