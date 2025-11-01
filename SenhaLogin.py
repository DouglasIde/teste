import pandas as pd

excel_file = "data.xlsx"

df = pd.read_excel(excel_file)

user_put = input("Digite seu username: ")
senha_put = input("Digite sua senha: ")

user = df[df["user"] == user_put]

if not user.empty:
    senha = user.iloc[0]['password']
    nome = user.iloc[0]['name']
    sobrenome = user.iloc[0]['last_name']

    if senha_put == senha:
        print(f"Bem-vindo {nome} {sobrenome}!!!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não encontrado!! Porfavor se cadastre no site")