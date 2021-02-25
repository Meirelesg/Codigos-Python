import pymysql

conexão = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'
)

cod = int(input("Isnira o código da disciplina: "))
disci = str(input("Qual o nome da disciplina: ")).lower()
des = str(input("Qual a descição da disciplina: ")).lower()
ch = int(input("Qual a carga horária da disciplina: "))

comando = "insert into disciplina values(%s,%s,%s,%s)"

valores = (cod,des,disci,ch)

consulta = conexão.cursor()
consulta.execute(comando,valores)

conexão.commit() #Gravar os dados no Banco Uaaaaau

print(consulta.rowcount,"linha(s) inserida com sucesso!")
conexão.close()