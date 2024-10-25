vendas = [] 
#SISTEMA DE VENDAS - FEITO POR VINICIUS CARDOSO

#Funçao para adicionar um dicionario de vendas numa lista
def adicionar_vendas(): 
    produto = input("Qual é o produto deseja escolher :")
    preco = float(input("Qual o preço do  produto: ")) 
    quantidade = float(input("Qual a quantidade do produto: ")) 
    data = input("Qual a data do produto (mm/dd/aa): ") 
    
    dicionario = {
        "entra_produto":produto,
        "entra_preco ":preco , 
        "entra_quantidade ": quantidade ,
        "entra_data": data
    }
    vendas.append(dicionario) #metodo para adicionar lista 
    
#Calcula o valor total das vendas
def total_vendas():
    soma = 0
    for i in vendas: 
        soma += i["entra_preco"] * i["entra_quantidade"] #Permite as váriaveis ficarem em escopo global 
        return soma
    
intervalo = 0   
def list_vendas(data_inicio , data_fim):
    for i in vendas:
        if i[data_inicio] >= i["entra_data"] and i[data_fim] <= i["entra_data"]:
            print("Qual é a data inicial  (mm/dd/aa): ")
            print("Qual é a data final (mm/dd/aa): ")  
            i[intervalo] = i[data_fim] - i[data_inicio]
            print("O intervalo entre as datas é :",i[intervalo]) 

def produto_mais_vendas():
    maior_valor = max(vendas, key=lambda x: x['entra_quantidade'])
    for i in vendas:
        if i['entra_quantidade'] == maior_valor['entra_quantidade']:
            print(f'\nProduto mais vendido: {i['entra_produto']} com {i['entra_quantidade']:.2f} unidades')



def menu():
    
    dicionario ={}

    while True: 
        print("1- Adicionar Vendas")
        print("2- Mostra o Total de vendas") 
        print("3- Listar vendas")
        print("4- Mostra o produto mais vendido ") 
        print("5- Sair do sistema")
        opcao = int(input("Informe qual a opção deseja escolher: ")) 
        match opcao:

            case 1:
                adicionar_vendas()

            case 2:
                print("Total de venda é", total_vendas())

            case 3:
                data_inicio = input('\nEntre com a data inicial da compra (mm/dd/aaaa): ')
                data_fim = input('Entre com a data final da compra (mm/dd/aaaa): ')
                list_vendas(data_inicio,data_fim)
                
            case 4:
                produto_mais_vendas()

            case 5:
                break 
            
if __name__ == '__main__':
    menu()
