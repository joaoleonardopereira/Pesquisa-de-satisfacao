print("Pesquisa de Satisfação - TudoWeb")

excelente = 0
bom = 0
ruim = 0

for i in range(50):
    print(f"\nEntrevistado {i+1}")

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    print("Avaliação do atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida!")

# Resultado final
print("\n=== RESULTADO DA PESQUISA ===")
print("Quantidade de EXCELENTE:", excelente)
print("Quantidade de BOM:", bom)
print("Quantidade de RUIM:", ruim)
