usuarios = {}

while True:
    while True:
        try:
            print("\n--- Cadastro de Usuário ---\n")
            username = input("Digite um nome de usuário: ").strip().lower()
            if username == "":
                print("Não deixe o campo vazio.")
            elif username in usuarios:
                print("Este nome de usuário já está sendo utilizado, tente outro.")
            else:
                break
        except Exception:
            print("Ocorreu um erro inesperado.")

    while True:
        try:
            idade = int(input(f"Olá {username}, me diga qual a sua idade: "))
            break
        except ValueError:
            print(f"{username}, digite um número válido.")

    while True:
        try:
            city = input(f"{username}, agora me diga qual é a sua cidade: ").strip()
            if city == "":
                print(f"{username}, não deixe este campo em branco.")
            else:
                break
        except Exception:
            print(f"Desculpa {username}, ocorreu um erro inesperado.")

    while True:
        try:
            email = input(f"{username}, digite seu email: ").strip()
            if "@" in email and "." in email:
                break
            else:
                print(f'{username}, o email deve conter "@" e ".".')
        except Exception:
            print(f"Desculpe {username}, ocorreu um erro inesperado.")

    usuarios[username] = {
        "Idade": idade,
        "Cidade": city,
        "Email": email
    }

    print(f"\nUsuário '{username}' cadastrado com sucesso!\n")
    continuar = input("Deseja cadastrar outro usuário? (sim/não): ").strip().lower()
    if continuar != "sim":
        break

print("\n--- Usuários Cadastrados ---\n")
for i, user in enumerate(usuarios, start=1):
    print(f"Usuário {i}:")
    print(f"  Nome: {user}")
    print(f"  Idade: {usuarios[user]['Idade']}")
    print(f"  Cidade: {usuarios[user]['Cidade']}")
    print(f"  Email: {usuarios[user]['Email']}")
    print("-----------------------------")

while True:
    try:
        pergunta = input("Deseja consultar algum usuário? (sim/não): ").strip().lower()
        if pergunta != "sim":
            break
        else:
            print("\n---Como deseja consultar---\n")
            print("1 - Por cidade")
            print("2 - Por idade mínima")
            print("3 - Por idade máxima")
            print("4 - Por faixa de idade")
            print("5 - Por nome")

            resposta = int(input("Escolha uma opção: ").strip())

            if resposta == 1:
                cidade = input("Digite o nome da cidade: ").strip().lower()
                encontrados = False
                for nome, dados in usuarios.items():
                    if dados["Cidade"].lower() == cidade:
                        print(f"\nNome: {nome}")
                        print(f"  Idade: {dados['Idade']}")
                        print(f"  Cidade: {dados['Cidade']}")
                        print(f"  Email: {dados['Email']}")
                        encontrados = True
                if not encontrados:
                    print(f"\nNenhum usuário encontrado na cidade: {cidade}")

            elif resposta == 2:
                idade_min = int(input("Digite a idade mínima: ").strip())
                encontrados = False
                for nome, dados in usuarios.items():
                    if dados["Idade"] >= idade_min:
                        print(f"\nNome: {nome}")
                        print(f"  Idade: {dados['Idade']}")
                        print(f"  Cidade: {dados['Cidade']}")
                        print(f"  Email: {dados['Email']}")
                        encontrados = True
                if not encontrados:
                    print(f"\nNenhum usuário encontrado com idade mínima de {idade_min}")

            elif resposta == 3:
                idade_max = int(input("Digite a idade máxima: ").strip())
                encontrados = False
                for nome, dados in usuarios.items():
                    if dados["Idade"] <= idade_max:
                        print(f"\nNome: {nome}")
                        print(f"  Idade: {dados['Idade']}")
                        print(f"  Cidade: {dados['Cidade']}")
                        print(f"  Email: {dados['Email']}")
                        encontrados = True
                if not encontrados:
                    print(f"\nNenhum usuário encontrado com idade máxima de {idade_max}")

            elif resposta == 4:
                idade_min = int(input("Digite a idade minima: "))
                idade_max = int(input("Digite a idade maxima: "))
                encontrados = False 
                for nome, dados in usuarios.items():
                    if idade_min <= dados["Idade"] <= idade_max:
                        print(f"\nNome: {nome}")
                        print(f"  Idade: {dados['Idade']}")
                        print(f"  Cidade: {dados['Cidade']}")
                        print(f"  Email: {dados['Email']}")
                        encontrados = True
                if not encontrados:
                    print(f"\nNenhum usuario encontrado na faixa de {idade_min} a {idade_max} anos")
            elif resposta == 5:
                nome_busca = input("Digite o nome: ")
                encontrados = False
                if nome_busca in usuarios:
                    dados = usuarios[nome_busca]
                    print(f"\nNome: {nome_busca}")
                    print(f"  Idade: {dados['Idade']}")
                    print(f"  Cidade: {dados['Cidade']}")
                    print(f"  Email: {dados['Email']}")
                else:
                    print(f"\nNenhum usuario {nome_busca} foi encontrado\n")
    except Exception:
        print("Ocorreu um erro durante a consulta.")