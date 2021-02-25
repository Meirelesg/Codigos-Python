import pymysql

#Estabelecer a conexão
'''
1º servidor
2º usuário
3º senha
4º O banco de Dados no MySQL
'''

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'
)
consulta = conexao.cursor() #O cursor permite interagir com o Banco de Dados Uaaaaau

sql = "select * from disciplina where carga_horaria >= 200"
consulta.execute(sql)

'''for itens in consulta:
    print(itens)
'''


#Hei de exibir consulta personalizada ;-----;
resultado = consulta.fetchall()

for itens in resultado:
    print(f"A disciplina {itens[2]} tem carga horária {itens[3]}h ")


conexao.close() #Encerrando a conexão Uaaaaaaaaaaaau