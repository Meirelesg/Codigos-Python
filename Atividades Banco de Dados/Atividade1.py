import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'ecommerce'
)

cod_produto = int(input("Insira um código para o produto: "))
nome = str(input("Insira o nome do produto: "))
descricao = str(input("Insira uma descrição do seu produto: "))
fabricante = str(input("Insira o nome do fabricante: "))
endereco = str(input("Insira o bairro do fabricante: "))

comando = "insert into produtos values(%s,%s,%s,%s,%s)"

valores = (cod_produto,nome,descricao,fabricante,endereco)

consulta = conexao.cursor()
consulta.execute(comando,valores)

conexao.commit()

print(consulta.rowcount,"Um novo produto adicionado!!")
conexao.close()