from collections import deque


class Vagao:
    def __init__(self, comprimento, peso):
        self.comprimento = comprimento
        self.peso = peso

    def imprime(self):
        print(
            f"Comprimento: {self.comprimento} m, Peso: {self.peso} toneladas")


class Locomotiva(Vagao):
    def __init__(self, comprimento, peso, potencia):
        super().__init__(comprimento, peso)
        self.potencia = potencia

    def imprime(self):
        super().imprime()
        print(f"Potência: {self.potencia} HP")


class VagaoPassageiros(Vagao):
    def __init__(self, comprimento, peso, num_passageiros):
        super().__init__(comprimento, peso)
        self.num_passageiros = num_passageiros

    def imprime(self):
        super().imprime()
        print(f"Número de passageiros: {self.num_passageiros}")


class VagaoCarga(Vagao):
    def __init__(self, comprimento, peso_total):
        super().__init__(comprimento, peso_total)
        self.carga = 0.75 * peso_total

    def imprime(self):
        super().imprime()
        print(f"Peso da carga: {self.carga} toneladas")


class ComposicaoFerroviaria(deque):
    def __init__(self):
        super().__init__()

    def carregar_de_arquivo(self, nome_arquivo):
        import pickle
        try:
            with open(nome_arquivo, 'rb') as f:
                self.extend(pickle.load(f))
            print("Composição carregada com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado. Criando uma nova composição.")
            self.gravar_no_arquivo(nome_arquivo)

    def gravar_no_arquivo(self, nome_arquivo):
        import pickle
        with open(nome_arquivo, 'wb') as f:
            pickle.dump(list(self), f)
        print("Composição salva com sucesso!")

    def inserir_vagao_frente(self, vagao):
        self.appendleft(vagao)
        print("Vagão inserido na frente.")

    def inserir_vagao_fim(self, vagao):
        self.append(vagao)
        print("Vagão inserido no final.")

    def remover_vagao_frente(self):
        if len(self) > 0:
            self.popleft()
            print("Vagão removido da frente.")
        else:
            print("A composição está vazia.")

    def remover_vagao_fim(self):
        if len(self) > 0:
            self.pop()
            print("Vagão removido do final.")
        else:
            print("A composição está vazia.")

    def diagnostico(self):
        total_peso = sum(vagao.peso for vagao in self)
        total_comprimento = sum(
            vagao.comprimento for vagao in self) + (len(self) - 1) * 2
        total_passageiros = sum(
            vagao.num_passageiros for vagao in self if isinstance(vagao, VagaoPassageiros))
        total_carga = sum(
            vagao.carga for vagao in self if isinstance(vagao, VagaoCarga))
        total_potencia = sum(
            vagao.potencia for vagao in self if isinstance(vagao, Locomotiva))

        print(f"Peso total da composição: {total_peso} toneladas")
        print(f"Comprimento total da composição: {total_comprimento} metros")
        print(f"Total de passageiros: {total_passageiros}")
        print(f"Total de carga: {total_carga} toneladas")
        print(f"Potência total: {total_potencia} HP")

        # Verificação de potência mínima
        if total_peso > 0:
            relacao_hp_por_ton = total_potencia / total_peso
            print(f"Relação HP/Ton: {relacao_hp_por_ton:.2f} HP/Ton")
            if relacao_hp_por_ton >= 1.05:
                print("Potência suficiente.")
            else:
                potencia_necessaria = 1.05 * total_peso
                potencia_faltante = potencia_necessaria - total_potencia
                print(
                    f"Potência insuficiente. Faltam {potencia_faltante:.2f} HP.")
        else:
            print("Não há peso suficiente para verificar a potência.")


def menu():
    composicao = ComposicaoFerroviaria()
    nome_arquivo = 'composicao.pkl'
    composicao.carregar_de_arquivo(nome_arquivo)

    while True:
        print("\n--- MENU ---")
        print("1. Inserir vagão (na frente)")
        print("2. Inserir vagão (no final)")
        print("3. Remover vagão (da frente)")
        print("4. Remover vagão (do final)")
        print("5. Diagnóstico da composição")
        print("6. Exibir dados do primeiro vagão")
        print("7. Exibir dados do último vagão")
        print("8. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            tipo = int(input(
                "Tipo de vagão (1 - Locomotiva, 2 - Passageiros, 3 - Carga): "))
            if tipo == 1:
                comprimento = float(input("Comprimento: "))
                peso = float(input("Peso: "))
                potencia = float(input("Potência: "))
                vagao = Locomotiva(comprimento, peso, potencia)
            elif tipo == 2:
                comprimento = float(input("Comprimento: "))
                peso = float(input("Peso: "))
                num_passageiros = int(input("Número de passageiros: "))
                vagao = VagaoPassageiros(comprimento, peso, num_passageiros)
            elif tipo == 3:
                comprimento = float(input("Comprimento: "))
                peso = float(input("Peso total: "))
                vagao = VagaoCarga(comprimento, peso)
            else:
                print("Opção inválida!")
                break

            composicao.inserir_vagao_frente(vagao)
            composicao.gravar_no_arquivo(nome_arquivo)

        elif opcao == 2:
            tipo = int(input(
                "Tipo de vagão (1 - Locomotiva, 2 - Passageiros, 3 - Carga): "))
            if tipo == 1:
                comprimento = float(input("Comprimento: "))
                peso = float(input("Peso: "))
                potencia = float(input("Potência: "))
                vagao = Locomotiva(comprimento, peso, potencia)
            elif tipo == 2:
                comprimento = float(input("Comprimento: "))
                peso = float(input("Peso: "))
                num_passageiros = int(input("Número de passageiros: "))
                vagao = VagaoPassageiros(comprimento, peso, num_passageiros)
            elif tipo == 3:
                comprimento = float(input("Comprimento: "))
                peso = float(input("Peso total: "))
                vagao = VagaoCarga(comprimento, peso)
            else:
                print("Opção inválida!")
                break

            composicao.inserir_vagao_fim(vagao)
            composicao.gravar_no_arquivo(nome_arquivo)

        elif opcao == 3:
            composicao.remover_vagao_frente()
            composicao.gravar_no_arquivo(nome_arquivo)

        elif opcao == 4:
            composicao.remover_vagao_fim()
            composicao.gravar_no_arquivo(nome_arquivo)

        elif opcao == 5:
            composicao.diagnostico()

        elif opcao == 6:
            if len(composicao) > 0:
                composicao[0].imprime()
            else:
                print("Composição vazia.")

        elif opcao == 7:
            if len(composicao) > 0:
                composicao[-1].imprime()
            else:
                print("Composição vazia.")

        elif opcao == 8:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()
