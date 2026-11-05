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
        return self.__num_motores

    def get_altitude_cruzeiro(self):
        return self.__altitude_cruzeiro

    def get_velocidade_maxima(self):
        return self.__velocidade_maxima

    def get_combustivel(self):
        return self.__combustivel

    def get_modelo(self):
        return self.__modelo

    def get_peso_decolagem(self):
        return self.__peso_decolagem

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
        print(f"Velocidade Limite: {self.get_velocidade_maxima()} km/h (Supersônico)")
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

