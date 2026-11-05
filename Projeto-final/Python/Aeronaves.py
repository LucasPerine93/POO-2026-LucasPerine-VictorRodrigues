import time
from abc import ABC, abstractmethod

class Aeronave:
    def __init__(self, modelo, num_motores, altitude_cruzeiro, velocidade_maxima, combustivel, peso_decolagem):

        self.__num_motores = num_motores
        self.__altitude_cruzeiro = altitude_cruzeiro
        self.__velocidade_maxima = velocidade_maxima
        self.__combustivel = combustivel
        self.__modelo = modelo
        self.__peso_decolagem = peso_decolagem

    def get_num_motores(self):
        return int(self.__num_motores)

    def get_altitude_cruzeiro(self):
        return int(self.__altitude_cruzeiro)

    def get_velocidade_maxima(self):
        return float(self.__velocidade_maxima)

    def get_combustivel(self):
        return int(self.__combustivel)

    def get_modelo(self):
        return self.__modelo

    def get_peso_decolagem(self):
        return str(self.__peso_decolagem)

    @abstractmethod
    def decolar(self):
        pass

    @abstractmethod
    def pousar(self):
        pass

    @abstractmethod
    def status_aeronave(self):
        pass

class AviaoMilitar(Aeronave):
    def __init__(self, modelo, num_motores, altitude_cruzeiro, velocidade_maxima, combustivel, peso_decolagem, armamentos):
        super().__init__(modelo, num_motores, altitude_cruzeiro, velocidade_maxima, combustivel, peso_decolagem)

        self.armamentos = armamentos

    def decolar(self):
        print("=" * 65)
        print(f"  INICIANDO PROTOCOLO DE DECOLAGEM TÁTICA: {self.get_modelo().upper()}")
        print("=" * 65)

        # 1. Checagens pré-voo
        print(f"Verificando pesos e combustível. TOW: {self.get_peso_decolagem()} kg | FOB: {self.get_combustivel()} kg.")
        time.sleep(1.2)

        print("Iniciando varredura e checagem dos pilones de armamento:")
        for arma in self.armamentos:
            print(f"  [ARMAMENTO] {arma} checado - SISTEMA TRAVADO E OPERACIONAL")
            time.sleep(0.6)

        print(f"Acionando {self.get_num_motores()} turbina(s) e checando controles fly-by-wire.")

        # 2. Alinhamento e liberação
        print("Alinhado na cabeceira da pista. Aguardando autorização do Controle Tático...")
        time.sleep(1.8)
        print("TORRE: Decolagem tática autorizada pista 01, vento calmo.", "ATC")
        time.sleep(1.0)

        # 3. Corrida na pista e velocidades de decisão
        v1 = int(self.get_velocidade_maxima() * 0.12)
        vr = int(self.get_velocidade_maxima() * 0.14)
        v2 = int(self.get_velocidade_maxima() * 0.17)

        print("Pós-combustores ligados! Manetes no máximo (FULL AFTERBURNER)!")
        for v in [
            print(f"100 nós - Pressão hidráulica e bocal checados (Velocidade: {int(v1 * 0.6)} kt)", 1.2),
            print(f"V1 atingida ({v1} kt) - Ponto de não-retorno", 1.5),
            print(f"VR ({vr} kt) - ROTACIONAR! Puxando manche", 1.2),
            print(f"V2 ({v2} kt) - Sustentação positiva e separação da pista", 1.0)
        ]:
            time.sleep(1.5)

        print("Subida vertical positiva. Trem de pouso recolhido (Gear Up).", "SISTEMAS")
        time.sleep(1.5)

        # 4. Subida até o nível de cruzeiro
        print(f"Subindo em ângulo tático até o teto de serviço ({self.get_altitude_cruzeiro()} ft)")

        print(f"Teto de serviço atingido: FL{self.get_altitude_cruzeiro() // 100}. SUCESSO")
        print(f"Radar em modo de combate varrendo a {self.get_velocidade_maxima()} km/h. INFO")
        print("=" * 65 + "\n")

    def pousar(self):
        print("=" * 65)
        print(f"  INICIANDO PROTOCOLO DE POUSO TÁTICO: {self.get_modelo().upper()}")
        print("=" * 65)

        # 1. Início da descida tática e checagens
        print(f"Iniciando descida tática a partir de FL{self.get_altitude_cruzeiro() // 100} ({self.get_altitude_cruzeiro()} ft).")
        combustivel_restante = int(self.get_combustivel() * 0.25)
        peso_pouso = int(self.get_peso_decolagem() * 0.70)
        print(f"Checando peso de pouso: {peso_pouso} kg | Combustível remanescente: {combustivel_restante} kg.")
        time.sleep(1.5)

        print("Travando pinos de segurança e desativando sistemas de ataque:")
        for arma in self.armamentos:
            print(f"  [SEGURANÇA] {arma} travado - MODO SEGURO ATIVADO")
            time.sleep(0.6)

        # 2. Aproximação tática e contato com o controle
        print("Ingressando no circuito militar (Overhead Break). Contatando Controle Tático...")
        time.sleep(1.8)
        print("TORRE TÁTICA: Autorizada quebra tática e aproximação pista 01, vento calmo.", "ATC")
        time.sleep(1.2)
        print("Quebra de alta energia executada. Aerofreios (Speedbrakes) abertos.")
        time.sleep(1.5)

        # 3. Configuração da aeronave e velocidades
        vref = int(self.get_velocidade_maxima() * 0.13)
        vapp = vref + 10

        print(f"Velocidade reduzida para aproximação final ({vapp} kt).")
        time.sleep(1.0)
        print("Flaps em posição de pouso. Paraquedas de frenagem (Drag Chute) armado.")
        time.sleep(1.2)
        print("Trem de pouso baixado e travado (Gear Down & Locked). Três verdes.", "SISTEMAS")
        time.sleep(1.5)
        print("TORRE TÁTICA: Pista 01 livre e desimpedida, autorizado pouso.", "ATC")
        time.sleep(1.5)

        # 4. Reta final e toque na pista (Callouts)
        etapas_final = [
            ("300 pés - Rampa visual alinhada no eixo (On Glideslope)", 1.2),
            ("100 pés - Mínimos checados, alinhamento visual perfeito", 1.0),
            ("50 pés - Manetes de potência em IDLE", 0.9),
            ("10 pés - Flare curto e atitude de impacto mantida", 0.8),
            ("TOUCHDOWN! Toque firme na pista 01", 1.0)
        ]

        for mensagem, pausa in etapas_final:
            print(mensagem)
            time.sleep(pausa)

        # 5. Desaceleração e dispersão para o abrigo blindado
        print("Aerofreios abertos e paraquedas de arrasto (Drag Chute) desdobrado!")
        time.sleep(1.5)
        print(f"Freios anti-skid atuando. Motores ({self.get_num_motores()}) desacelerando.")
        time.sleep(1.8)
        print("Paraquedas ejetado na pista. Aeronave sob velocidade de táxi controlada.")
        time.sleep(1.2)
        print("Livrando pista ativa via taxiway tática. Contatando Controle de Solo.", "SOLO")
        time.sleep(1.0)
        print("Aeronave recolhida no hangar blindado (HAS). Turbinas cortadas. Missão cumprida!", "SUCESSO")
        print("=" * 65 + "\n")

    def status_aeronave(self):
        print("=" * 65)
        print(f"  PAINEL DE STATUS OPERACIONAL E TÁTICO: {self.get_modelo().upper()}")
        print("=" * 65)

        # 1. Telemetria e Propulsão
        print(f"Aeronave: {self.get_modelo().upper()} | Configuração: TÁTICA MILITAR")
        print(f"Propulsão: {self.get_num_motores()} turbina(s) com pós-combustor | Status: OPERACIONAL")
        print(f"Peso Total (TOW): {self.get_peso_decolagem()} kg | Combustível FOB: {self.get_combustivel()} kg")
        time.sleep(1.0)

        # 2. Performance e Aviônica
        print(f"Teto Operacional: FL{self.get_altitude_cruzeiro() // 100} ({self.get_altitude_cruzeiro()} ft)")
        print(f"Velocidade Limite: {self.get_velocidade_maxima()} MACH (Supersônico)")
        print("Sistemas Aviônicos: Radar AESA ativo | RWR operacional | ECM ligado")
        time.sleep(1.2)

        # 3. Varredura do Inventário de Armamentos
        print("-" * 65)
        print("INVENTÁRIO BÉLICO E STATUS DOS PILONES:")
        for i, arma in enumerate(self.armamentos, start=1):
            print(f"  [PILONE {i:02d}] {arma} - MUNIÇÃO CHECADA / PRONTO PARA DISPARO")
            time.sleep(0.5)
        print("-" * 65)
        time.sleep(1.0)

        # 4. Prontidão Tática e Contramedidas
        print("Contramedidas defensivas: Chaff & Flare armados e checados.", "DEFESA")
        time.sleep(0.8)
        print("DataLink / IFF: Resposta tática integrada ao comando aéreo.", "COMMS")
        time.sleep(0.8)
        print("DIAGNÓSTICO FINAL: Todos os subsistemas verdes. Pronto para combate!", "PRONTO")
        print("=" * 65 + "\n")

class AviaoComercial(Aeronave):
    def __init__(self, modelo, num_motores, altitude_cruzeiro, velocidade_maxima, combustivel, peso_decolagem, numero_assentos):
            super().__init__(modelo, num_motores, altitude_cruzeiro, velocidade_maxima, combustivel, peso_decolagem)
    
            self.numero_assentos = numero_assentos

    def decolar(self):
        print("=" * 65)
        print(f"   INICIANDO PROTOCOLO DE DECOLAGEM COMERCIAL: {self.get_modelo().upper()}")
        print("=" * 65)

        # 1. Procedimentos de cabine e pré-voo
        print(f"Aeronave comercial configurada para {self.numero_assentos} assentos.")
        print(f"Cálculo de despacho - TOW: {self.get_peso_decolagem()} kg | FOB: {self.get_combustivel()} kg.")
        time.sleep(1.2)

        print(f"Embarque concluído ({self.numero_assentos} passageiros a bordo).")
        print("CHEFE DE CABINE: 'Portas em automático, travar escorregadores e cross-check.'")
        time.sleep(1.0)
        print("Demonstração de segurança e briefing de saídas de emergência concluídos.")
        time.sleep(1.0)

        # 2. Pushback, acionamento e táxi
        print("Pushback e reboque concluídos no gate. Beacon acionado.")
        print(f"Acionando {self.get_num_motores()} motor(es) turbofan com fluxo suave.")
        time.sleep(1.5)
        print("Flaps configurados para decolagem. Spoilers armados. Táxi até a pista ativa.")
        time.sleep(1.5)
        print("TORRE: Decolagem comercial autorizada, pista 09R, vento 080 a 10 nós.", "ATC")
        time.sleep(1.0)

        # 3. Corrida de pista e velocidades operacionais
        v1 = int(self.get_velocidade_maxima() * 0.15)
        vr = int(self.get_velocidade_maxima() * 0.17)
        v2 = int(self.get_velocidade_maxima() * 0.20)

        print("Potência de decolagem ajustada (FLEX/TOGA). Corrida iniciada.")
        etapas_decolagem = [
            (f"80 nós - Instrumentos checados, aceleração simétrica ({int(v1 * 0.6)} kt)", 1.2),
            (f"V1 atingida ({v1} kt) - Velocidade de decisão, decolagem comprometida", 1.4),
            (f"VR ({vr} kt) - ROTACIONAR! Subida suave iniciada", 1.2),
            (f"V2 ({v2} kt) - Velocidade de segurança e razão de subida positiva", 1.0)
        ]

        for mensagem, pausa in etapas_decolagem:
            print(mensagem)
            time.sleep(pausa)

        print("Razão positiva confirmada. Trem de pouso recolhido (Gear Up).", "SISTEMAS")
        time.sleep(1.5)

        # 4. Subida, pressurização e nível de cruzeiro
        print(f"Subida padrão via saída por instrumentos (SID) até FL{self.get_altitude_cruzeiro() // 100}.")
        print("Altitude de cabine estabilizada a 7.500 ft (Pressurização normal).")
        time.sleep(1.2)
        print(f"Nível de cruzeiro atingido: FL{self.get_altitude_cruzeiro() // 100} ({self.get_altitude_cruzeiro()} ft).")
        print(f"Velocidade de cruzeiro mantida a {self.get_velocidade_maxima() * 0.82:.0f} km/h (Mach econômico).")
        print("Sinal de atar cintos desligado. Serviço de bordo liberado para os passageiros.")
        print("=" * 65 + "\n")

    def pousar(self):
        print("=" * 65)
        print(f"   INICIANDO PROTOCOLO DE POUSO COMERCIAL: {self.get_modelo().upper()}")
        print("=" * 65)

        # 1. Top of Descent (TOD) e preparação da cabine
        print(f"Início da descida a partir de FL{self.get_altitude_cruzeiro() // 100} ({self.get_altitude_cruzeiro()} ft).")
        combustivel_restante = int(self.get_combustivel() * 0.22)
        peso_pouso = int(self.get_peso_decolagem() * 0.78)
        print(f"Peso estimado de pouso (MLW): {peso_pouso} kg | Combustível remanescente: {combustivel_restante} kg.")
        time.sleep(1.2)

        print("PILOTO: 'Tripulação de cabine, preparar para o pouso.'")
        print(f"Comissários verificam os {self.numero_assentos} assentos: poltronas na vertical e mesas travadas.")
        time.sleep(1.2)

        # 2. Aproximação por instrumentos e contato ATC
        print("Ingressando no procedimento de chegada STAR e alinhando com o ILS.")
        time.sleep(1.5)
        print("TORRE: Autorizada aproximação ILS pista 09R. Vento calmo, altímetro 1013 hPa.", "ATC")
        time.sleep(1.2)

        # 3. Configuração de aproximação final
        vref = int(self.get_velocidade_maxima() * 0.14)
        vapp = vref + 5

        print(f"Reduzindo para velocidade de aproximação (Vapp: {vapp} kt).")
        time.sleep(1.0)
        print("Flaps Full estendidos. Speedbrakes armados e autobrakes selecionados.")
        time.sleep(1.2)
        print("Trem de pouso baixado e travado (Gear Down & Locked). Três verdes confirmados.", "SISTEMAS")
        time.sleep(1.5)
        print("TORRE: Pista livre. Voo autorizado para pouso.", "ATC")
        time.sleep(1.2)

        # 4. Reta final e toque (Callouts)
        etapas_pouso = [
            ("500 pés - Aproximação estabilizada, piloto automático desconectado", 1.2),
            ("100 pés - Mínimos visuais atingidos, pista à vista", 1.0),
            ("50 pés - Manetes de potência em IDLE", 0.8),
            ("20 pés - Arredondamento (Flare) suave", 0.8),
            ("TOUCHDOWN! Toque suave na zona de contato da pista 09R", 1.0)
        ]

        for mensagem, pausa in etapas_pouso:
            print(mensagem)
            time.sleep(pausa)

        # 5. Desaceleração, táxi e desembarque
        print("Reversores acionados e ground spoilers abertos automaticamente.")
        time.sleep(1.4)
        print(f"Autobrakes e freios desacelerando os {self.get_num_motores()} motor(es).")
        time.sleep(1.5)
        print("Reversores recolhidos a 60 nós. Aeronave em velocidade de táxi controlada.")
        time.sleep(1.0)
        print("Livrando a pista via taxiway rápida. Contatando o Controle de Solo.", "SOLO")
        time.sleep(1.2)
        print(f"Acoplado ao finger no Terminal de Passageiros. Motores cortados.")
        print(f"CHEFE DE CABINE: 'Portas em manual, desarmar escorregadores.' Desembarque dos {self.numero_assentos} passageiros iniciado.")
        print("=" * 65 + "\n")

    def status_aeronave(self):
        print("=" * 65)
        print(f"   PAINEL DE STATUS OPERACIONAL E CABINE: {self.get_modelo().upper()}")
        print("=" * 65)

        # 1. Telemetria e Motores
        print(f"Aeronave: {self.get_modelo().upper()} | Operação: TRANSPORTE DE PASSAGEIROS")
        print(f"Propulsão: {self.get_num_motores()} turbofan(s) comerciais de alto bypass | Status: OPERACIONAL")
        print(f"Capacidade de Carga: TOW máx {self.get_peso_decolagem()} kg | Combustível FOB: {self.get_combustivel()} kg")
        time.sleep(1.0)

        # 2. Performance e Navegação
        print(f"Teto de Cruzeiro Homologado: FL{self.get_altitude_cruzeiro() // 100} ({self.get_altitude_cruzeiro()} ft)")
        print(f"Velocidade Limite (VMO/MMO): {self.get_velocidade_maxima()} MACH")
        print("Sistemas Aviônicos: TCAS II integrado | FMS/RNAV calibrado | Weather Radar ativo")
        time.sleep(1.2)

        # 3. Cabine e Conforto dos Passageiros
        print("-" * 65)
        print("CONFIGURAÇÃO DA CABINE E SERVIÇO:")
        print(f"  [ASSENTOS] Capacidade Total: {self.numero_assentos} poltronas homologadas")
        print("  [PRESSURIZAÇÃO] Válvula Outflow em modo automático (8.000 ft máx)")
        print("  [SISTEMAS] Iluminação de cabine, IFE (Entretenimento) e Galleys checados")
        print("  [SEGURANÇA] Máscaras de oxigênio de passageiros e escorregadores armados")
        print("-" * 65)
        time.sleep(1.0)

        # 4. Prontidão para o Próximo Voo (Turnaround)
        print("Suprimentos de solo: GPU e ar condicionado externo desconectados.", "SOLO")
        time.sleep(0.8)
        print("Briefing de despacho: Plano de voo IFR e manifesto de carga assinados.", "DESPACHO")
        time.sleep(0.8)
        print("DIAGNÓSTICO FINAL: Aeronavegabilidade 100%. Pronta para a malha aérea regular!", "PRONTO")


avioes = []

def exibir_opcoes():
    print("0. Sair")
    print("1. Cadastrar aviao militar")
    print("2. Cadastrar aviao comercial")
    print("3. Exibir status de todos os avioes")

def main():
    while True:
        exibir_opcoes()
        try: 
            modo = int(input("Digite um numero: "))
        except ValueError:
            print("[ERRO]: Digite apenas números inteiros e válidos\n")

        if modo == 0:
            print("Saindo...")
            break
        elif modo == 1:
            cadastrar_aviao_militar()
        elif modo == 2:
            cadastrar_aviao_comercial()
        elif modo == 3:
            exibir_status_avioes()
        else:
            print("[ERRO]: Modo invalido")

def exibir_status_avioes():
    for aviao in avioes:
        aviao.status_aeronave()

def cadastrar_aviao_comercial():
    try:
        modelo = str(input("Digite o modelo da aeronave: ")).strip()
        if not modelo:
            raise ValueError("[ERRO]: Preencha o modelo corretamente")

        num_motores = input("Digite o numero de motores da aeronave: ").strip()
        if not num_motores or not num_motores.isdigit() or int(num_motores) < 1:
            raise ValueError("[ERRO]: São aceitos somente numeros maiores que 1 neste campo")
        
        altitude_cruzeiro = input("Digite a altitude de cruzeiro da aeronave: ").strip()
        if not altitude_cruzeiro or not altitude_cruzeiro.isdigit() or int(altitude_cruzeiro) < 400 :
            raise ValueError("[ERRO]: São aceitos somente numeros maiores que 400 neste campo")

        velocidade_maxima = input("Digite a velocidade maxima da aeronave (MACH): ").strip()
        if not velocidade_maxima or not velocidade_maxima.replace('.', '', 1).isdecimal() or 1.0 >= float(velocidade_maxima) < 0.1:
            raise ValueError("[ERRO]: São aceitos somente numeros maiores que 0.1 e menores que 1.0 neste campo")

        combustivel = input("Digite quantas libras de combustivel sua aeronave tem: ").strip()
        if not combustivel or not combustivel.isdigit() or int(combustivel) <= 0:
            raise ValueError("[ERRO]: Numero inválido para o combustivel")

        peso_decolagem = input("Digite o peso de decolagem em kg de sua aeronave: ").strip()
        if not peso_decolagem or not peso_decolagem.isdigit() or int(peso_decolagem) < 2100 :
            raise ValueError("[ERRO]: Peso de decolagem invalido, deve ser maior que 2100kg")

        numero_assentos = input("Digite o numero de assentos de sua aeronave: ")
        if not numero_assentos or numero_assentos.isdigit() or int(numero_assentos) <= 0:
            raise ValueError("[ERRO]: O numero de assentos deve ser maior que 0")

        novo_aviao = AviaoComercial(modelo, num_motores, altitude_cruzeiro, velocidade_maxima, combustivel, peso_decolagem, numero_assentos)
        avioes.append(novo_aviao)
        print("[SUCESSO]: Avião cadastrado com sucesso!")
    except ValueError as erro:
        print(erro)
        return


def cadastrar_aviao_militar():
    try:
        modelo = str(input("Digite o modelo da aeronave: ")).strip()
        if not modelo:
            raise ValueError("[ERRO]: Preencha o modelo corretamente")

        num_motores = input("Digite o numero de motores da aeronave: ").strip()
        if not num_motores or not num_motores.isdigit() or int(num_motores) < 1:
            raise ValueError("[ERRO]: São aceitos somente numeros maiores que 1 neste campo")
        
        altitude_cruzeiro = input("Digite a altitude de cruzeiro da aeronave: ").strip()
        if not altitude_cruzeiro or not altitude_cruzeiro.isdigit() or int(altitude_cruzeiro) < 100:
            raise ValueError("[ERRO]: São aceitos somente numeros maiores que 100 neste campo")

        velocidade_maxima = input("Digite a velocidade maxima da aeronave (MACH): ").strip()
        if not velocidade_maxima or not velocidade_maxima.replace('.', '', 1).isdecimal() or float(velocidade_maxima) < 0.1:
            raise ValueError("[ERRO]: São aceitos somente numeros maiores que 0.1 neste campo")

        combustivel = input("Digite quantas libras de combustivel sua aeronave tem: ").strip()
        if not combustivel or not combustivel.isdigit() or int(combustivel) <= 0:
            raise ValueError("[ERRO]: Numero inválido para o combustivel")

        peso_decolagem = input("Digite o peso de decolagem em kg de sua aeronave: ").strip()
        if not peso_decolagem or not peso_decolagem.isdigit() or int(peso_decolagem) < 2500:
            raise ValueError("[ERRO]: Peso de decolagem invalido, deve ser maior que 2500kg")

        print("============================================")
        print("=== DIGITE OS ARMAMENTOS DE SUA AERONAVE ===")
        print("============================================")

        print("[AVISO]: Para parar de cadastrar armamentos, digite 'parar'")

        verificar_parada = None
        indice_armamento = 1
        armamentos = []
        while verificar_parada != "parar":
            armamento = input(f"{indice_armamento}° armamento: ").strip()
            if not armamento:
                print("[ERRO]: Digite um armamento para continuar!")
                continue

            armamentos.append(armamento)
            indice_armamento += 1
            verificar_parada = armamento.lower()

        novo_aviao = AviaoMilitar(modelo, num_motores, altitude_cruzeiro, velocidade_maxima, combustivel, peso_decolagem, armamentos)
        avioes.append(novo_aviao)
        print("[SUCESSO]: Avião cadastrado com sucesso!")
    except ValueError as erro:
        print(erro)
        return
    
if __name__ == "__main__":
    main()