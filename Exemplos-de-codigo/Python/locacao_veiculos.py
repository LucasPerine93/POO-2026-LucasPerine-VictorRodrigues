from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.__modelo = modelo
        self.__placa = placa
        self.__valor_diaria = valor_diaria

    def get_modelo(self) -> str:
        return self.__modelo

    def get_placa(self) -> str:
        return self.__placa

    def get_valor_diaria(self) -> int:
        return self.__valor_diaria

    def set_modelo(self, novo_modelo: str):
        if not isinstance(novo_modelo, str):
            raise TypeError("[ERRO]: O valor informado deve ser um texto!")
        
        if novo_modelo != self.__modelo:
            print(f"Modelo: {self.__modelo} alterado para {novo_modelo} com sucesso")
            self.__modelo = novo_modelo
        else:
            raise ValueError(f"[ERRO]: O modelo {self.__modelo} já tem esse nome, para alterar coloque um dado diferente")

    def set_placa(self, nova_placa: str):
        if not isinstance(nova_placa, str):
            raise TypeError("O valor informado deve ser um texto!")
        
        if nova_placa != self.__placa:
            print(f"Placa: {self.__placa} alterada para {nova_placa} com sucesso")
            self.__placa = nova_placa

        else:
            raise ValueError(f"[ERRO]: A placa {self.__placa} já tem esse código, para alterar coloque um código diferente")

    def set_valor_diaria(self, novo_valor: int):
        if not isinstance(novo_valor, int):
            raise TypeError("[ERRO]: O valor informado deve ser um número!")
        
        if novo_valor > 0:
            print(f"Valor: R${self.__valor_diaria:.2f} alterado para R${novo_valor:.2f} com sucesso")
            self.__valor_diaria = novo_valor

        else:
            raise ValueError(f"[ERRO]: O valor da diária deve ser maior que 0")

    @abstractmethod
    def calcular_aluguel(self, dias):
        pass

    @abstractmethod
    def imprimir_status(self):
        pass

class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)

        self.portas = portas
        self.__taxa_fixa = 50

    def calcular_aluguel(self, dias):
        if not isinstance(dias, int):
            raise TypeError("[ERRO]: O valor informado deve ser um número!")
        
        if dias > 0:
            valor = (dias * self.get_valor_diaria()) + self.__taxa_fixa

            print(f"\nO carro de modelo: {self.get_modelo()}, foi alugado por {dias} dias\n")
            print("------------ RESUMO ------------")
            print(f"Valor alugado: R${valor:.2f}")
            print(f"Taxa de limpeza: R${self.__taxa_fixa}")
            print(f"Dias com o carro: {dias} dias")
            print(f"Configuração: carro com {self.portas} portas")
            print("--------------------------------")

        else:
            raise ValueError(f"[ERRO]: Os dias selecionados são menores ou iguais a 0")

    def imprimir_status(self):
        print("\n================= STATUS DO CARRO =================")
        print(f"Modelo:            {self.get_modelo()}")
        print(f"Placa:             {self.get_placa()}")
        print(f"Portas:            {self.portas}")
        print(f"Valor da Diária:   R${self.get_valor_diaria():.2f}")
        print(f"Taxa de Limpeza:   R${self.__taxa_fixa:.2f}")
        print("===================================================")

class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)

        self.cilindradas = cilindradas
        self.__taxa_fixa = 10

    def calcular_aluguel(self, dias):
        if not isinstance(dias, int):
            raise TypeError("[ERRO]: O valor informado deve ser um número!")
        
        if dias > 0:
            valor = (dias * self.get_valor_diaria())
            valor_com_taxa = valor - ((self.__taxa_fixa / 100) * valor)

            print(f"\nA moto de modelo: {self.get_modelo()}, foi alugada por {dias} dias\n")
            print("------- RESUMO -------")
            print(f"Valor alugado: R${valor_com_taxa:.2f}")
            print(f"Taxa de desconto: {self.__taxa_fixa}%")
            print(f"Dias com a moto: {dias} dias")
            print(f"Configuração: moto com {self.cilindradas} cilindradas")
            print("----------------------")
        
        else:
            raise ValueError(f"[ERRO]: Os dias selecionados são menores ou iguais a 0")

    def imprimir_status(self):
        print("\n================= STATUS DA MOTO ==================")
        print(f"Modelo:            {self.get_modelo()}")
        print(f"Placa:             {self.get_placa()}")
        print(f"Cilindradas:       {self.cilindradas} cc")
        print(f"Valor da Diária:   R$ {self.get_valor_diaria():.2f}")
        print(f"Taxa de Desconto:  {self.__taxa_fixa}%")
        print("===================================================")

veiculos = [
    Carro("Corola", "BHU-0935", 150, 4),
    Carro("Ferrari", "FER-9393", 930, 2),
    Moto("Tiger", "TIG-9373", 80, 800),
    Moto("Panigale", "DUC-9393", 293, 1000)
]

def exibir_opcoes():
    print("\n1. Simular aluguel da frota inteira")
    print("2. Cadastrar novo carro")
    print("3. Cadastrar nova moto")
    print("4. Buscar veículo pela placa")
    print("0. Sair\n")


def main():
    while True:
        exibir_opcoes()

        try:
            opcao = int(input("Digite um número: "))
        except (ValueError, TypeError):
            print("[ERRO]: Digite apenas números inteiros e válidos\n")
            continue

        if opcao == 1:
            simular_aluguel()

        elif opcao == 2:
            cadastrar_veiculo(1)

        elif opcao == 3:
            cadastrar_veiculo(2)

        elif opcao == 4:
            buscar_veiculo()

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("[ERRO]: Opção inexistente no menu\n")

def simular_aluguel():
    try:
        dias = int(input("Para quantos dias: "))
        if dias is None or dias <= 0:
            raise ValueError()
    except (ValueError, TypeError):
        print("[ERRO]: Digite apenas números inteiros e válidos\n")
        return
    
    try:
        for i in veiculos:
            i.calcular_aluguel(dias)
    except (ValueError, TypeError) as e:
        print(e)

def cadastrar_veiculo(tipo_veiculo: int):
    try:
        modelo_novo = str(input("Digite o modelo: "))
        if not modelo_novo.strip():
            raise ValueError()

        if not isinstance(modelo_novo, str):
            raise TypeError("[ERRO]: Digite um tipo válido para modelo (string)")
        
    except (ValueError, TypeError):
        print("[ERRO]: Digite um nome válido para o modelo\n")
        return

    try:
        placa_nova = str(input("Digite a placa: "))
        if not placa_nova.strip():
            raise ValueError("[ERRO]: Digite uma placa válida!\n")

        if not isinstance(placa_nova, str):
            raise TypeError("[ERRO]: Digite um tipo válido para placa (string)")
        
        for i in veiculos:
            placa_frota = i.get_placa()

            if placa_frota == placa_nova:
                raise ValueError("[ERRO]: Essa placa já existe na frota!")

    except (ValueError, TypeError) as e:
        print(e)
        return

    try:
        valor_diaria = int(input("Digite o valor da diária: "))
        if valor_diaria is None or valor_diaria <= 0:
            raise ValueError()
        
    except (ValueError, TypeError):
        print("[ERRO]: Digite um valor inteiro e válido para a diária!\n")
        return
    
    try:
        if tipo_veiculo == 1:
            valor_personalizado = int(input("Digite o número de portas: "))

        if tipo_veiculo == 2:
            valor_personalizado = int(input("Digite o número de cilindradas: "))

        if valor_personalizado is None or valor_personalizado <= 0:
            raise ValueError()
        
    except (ValueError, TypeError):
        if tipo_veiculo == 1:
            print("[ERRO]: Digite um valor inteiro e válido para as portas!\n")

        if tipo_veiculo == 2:
            print("[ERRO]: Digite um valor inteiro e válido para as cilindradas!\n")

        return

    if tipo_veiculo == 1:
        novo_carro = Carro(modelo=modelo_novo, placa=placa_nova, valor_diaria=valor_diaria, portas=valor_personalizado)
        veiculos.append(novo_carro)
        print("\n[SUCESSO]: Carro cadastrado com sucesso")

    if tipo_veiculo == 2:
        nova_moto = Moto(modelo=modelo_novo, placa=placa_nova, valor_diaria=valor_diaria, cilindradas=valor_personalizado)
        veiculos.append(nova_moto)
        print("\n[SUCESSO]: Moto cadastrada com sucesso")

def buscar_veiculo():
    try:
        placa_alvo = str(input("Digite a placa do veículo: "))
        if not placa_alvo.strip():
            raise ValueError("[ERRO]: Digite algo para buscar o veículo")

        if not isinstance(placa_alvo, str):
            raise TypeError("[ERRO]: Insira dados válidos para buscar (string)")
        
        for i in veiculos:
            placa = i.get_placa()

            if placa_alvo.upper() == placa:
                i.imprimir_status()
                return
        else:
            print("[ERRO]: Placa não encontrada")

    except (ValueError, TypeError) as  e:
        print(e)
        return

if __name__ == "__main__":
    main()