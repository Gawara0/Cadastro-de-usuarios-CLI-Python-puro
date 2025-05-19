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
		pergunta = input("deseja consultar algum usuario? (sim/nao)").strip().lower()
		if pergunta != "sim":
			break
		else:
			pesquisa = input("digite o nome do usuario: ").strip().lower()
			if pesquisa in usuarios:
				print(f"  Nome: {pesquisa}")
				print(f"  Idade: {usuarios[pesquisa]['Idade']}")
				print(f"  Cidade: {usuarios[pesquisa]['Cidade']}")
				print(f"  Email: {usuarios[pesquisa]['Email']}")
	except Exception:
			print ("Ocorreu um erro inesperado")