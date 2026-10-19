#include <iostream>
#include <iomanip>
#include <string>
#include <memory>
#include <stdexcept>
#include <vector>

enum class OpcaoAtual {
    SIMULAR_ALUGUEL = 1,
    CADASTRAR_CARRO = 2,
    CADASTRAR_MOTO = 3,
    BUSCAR_VEICULO = 4,
    SAIR = 0

};

enum class ModelosFrota {
    CARRO = 1,
    MOTO = 2 
};

class Veiculo {
private:
    std::string modelo;
    std::string placa;
    double valor_diaria;

public:
    Veiculo (std::string m, std::string p, double vd)
        : modelo(m), placa(p), valor_diaria(vd) {}

    virtual ~Veiculo() = default;

    std::string get_modelo() const {
        return modelo;
    }

    std::string get_placa() const {
        return placa;
    }

    double get_valor_diaria() const {
        return valor_diaria;
    }

    void set_modelo(const std::string& novo_modelo) {
        if (novo_modelo == modelo) {
            throw std::invalid_argument("[ERRO]: O modelo digitado ja tem esse nome, para alterar coloque um dado diferente");
        }

        else {
            modelo = novo_modelo;
            std::cout << "[SUCESSO]: Modelo alterado com sucesso";
        }
    }

    void set_placa(const std::string& nova_placa) {
        if (nova_placa == placa) {
            throw std::invalid_argument("[ERRO]: A placa digitada ja tem esse codigo, para alterar coloque um código diferente");
        }

        else {
            placa = nova_placa;
            std::cout << "[SUCESSO]: Placa alterada com sucesso";
        }
    }

    void set_valor_diaria(const double novo_valor) {
        if (novo_valor <= 0) {
            throw std::invalid_argument("[ERRO]: O valor da diaria deve ser maior que 0");
        }

        else {
            valor_diaria = novo_valor;
            std::cout << "[SUCESSO]: O valor da diaria foi alterado";
        }
    }

    virtual void calcular_aluguel(const int dias) = 0;
    virtual void imprimir_status() const = 0;

};

class Carro : public Veiculo {
private:
    double taxa_fixa = 50.0;
    int portas;

public:
    Carro (std::string m, std::string p, double vd, int pt) 
        : Veiculo(m, p, vd), portas(pt) {}

    void calcular_aluguel(const int dias) override {
        if (dias <= 0) {
            throw std::invalid_argument("[ERRO]: Os dias selecionados sao menores ou iguais a 0");
        }

        else {
            double valor = (dias * get_valor_diaria()) + taxa_fixa;

            std::cout << "\nO carro de modelo: " << get_modelo() << ", foi alugado por " << dias << " dias\n\n";

            std::cout << "------------ RESUMO ------------\n"
                      << "Valor alugado: R$" << std::fixed << std::setprecision(2) << valor << "\n"
                      << "Taxa de limpeza: R$" << taxa_fixa << "\n"
                      << "Dias com o carro: " << dias << " dias\n"
                      << "Configuracao: carro com " << portas << " portas\n"
                      << "--------------------------------\n";
        }
    }

    void imprimir_status() const override {
        std::cout << "\n================= STATUS DO CARRO =================\n"
                  << "Modelo:            " << get_modelo() << "\n"
                  << "Placa:             " << get_placa() << "\n"
                  << "Portas:            " << portas << "\n"
                  << "Valor da Diaria:   R$" << std::fixed << std::setprecision(2) << get_valor_diaria() << "\n"
                  << "Taxa de Limpeza:   R$" << std::fixed << std::setprecision(2) << taxa_fixa << "\n"
                  << "===================================================\n";
    }
};

class Moto : public Veiculo {
private:
    int cilindradas;
    double desconto_fixo = 10.0;

public:
    Moto(std::string m, std::string p, double vd, int cc)
        : Veiculo(m, p, vd), cilindradas(cc) {}

    void calcular_aluguel(const int dias) override {
        if (dias <= 0) {
            throw std::invalid_argument("[ERRO]: Os dias selecionados são menores ou iguais a 0");
        }
        
        else {
            double valor = (dias * get_valor_diaria());
            double valor_com_desconto = valor - (valor * (desconto_fixo / 100));

            std::cout << "\nA moto de modelo: " << get_modelo() << ", foi alugada por " << dias << " dias\n\n";

            std::cout << "------- RESUMO -------\n"
                      << "Valor alugado: R$" << std::fixed << std::setprecision(2) << valor_com_desconto << "\n"
                      << "Taxa de desconto: " << desconto_fixo << "%\n"
                      << "Dias com a moto: " << dias << " dias\n"
                      << "Configuracao: moto com " << cilindradas << " cilindradas\n"
                      << "----------------------\n";
        }
    }

    void imprimir_status() const override {
        std::cout << "\n================= STATUS DA MOTO ==================\n"
                  << "Modelo:            " << get_modelo() << "\n"
                  << "Placa:             " << get_placa() << "\n"
                  << "Cilindradas:       " << cilindradas << " cc\n"
                  << "Valor da Diaria:   R$ " << std::fixed << std::setprecision(2) << get_valor_diaria() << "\n"
                  << "Taxa de Desconto:  " << desconto_fixo << "%\n"
                  << "===================================================\n";
    }
};

std::vector<std::unique_ptr<Veiculo>> veiculos;

int stringToInt(const std::string& valor) {

    if (valor.empty()) {
        throw std::invalid_argument("[ERRO]: Campo de texto vazio");
    }

    try {
        return std::stoi(valor);
    }
    catch (const std::invalid_argument& e) {
        throw std::invalid_argument("[ERRO]: Digite apenas numeros inteiros validos\n");
    }
    catch (const std::out_of_range& e) {
        throw std::invalid_argument("\n[ERRO]: Numero grande demais\n");
    }
}

void simular_aluguel() {
    try {
        std::string entrada;
        std::cout << "Para quantos dias: ";
        std::getline(std::cin, entrada);

        if (entrada.empty()) {
            throw std::invalid_argument("[ERRO]: Digite algo no campo de texto");
        }

        int dias = stringToInt(entrada);
        
        for (const auto& v : veiculos) {
            v->calcular_aluguel(dias);
        }
    }
    catch (const std::invalid_argument& e) {
        std::cout << "\n" << e.what() << "\n\n";
        return; 
    }
}

void cadastrar_veiculo(const int modo) {
    try {
        std::string modelo, placa, vd, vp;

        std::cout << "Digite o modelo: ";
        std::getline(std::cin, modelo);

        if (modelo.empty()) {
            throw std::invalid_argument("[ERRO]: Digite algo no campo de texto");
        }


        std::cout << "Digite a placa: ";
        std::getline(std::cin, placa);

        if (placa.empty()) {
            throw std::invalid_argument("[ERRO]: Digite algo no campo de texto");
        }
        
        for (const auto& p : veiculos) {
            if (placa == p->get_placa()) {
                throw std::invalid_argument("[ERRO]: Essa placa ja existe na frota");
            }
        }

        std::cout << "Digite o valor da diaria: ";
        std::getline(std::cin, vd);

        int valor_diaria = stringToInt(vd);
        if (valor_diaria <= 0) {
            throw std::invalid_argument("[ERRO]: O valor da diaria deve ser maior que 0");
        }

        if (static_cast<ModelosFrota>(modo) == ModelosFrota::CARRO) {
            std::cout << "Digite quantas portas o carro tem: ";
        } 
        if (static_cast<ModelosFrota>(modo) == ModelosFrota::MOTO) {
            std::cout << "Digite cilindradas a moto tem: ";
        }

        std::getline(std::cin, vp);
        if (vp.empty()) {
            throw std::invalid_argument("[ERRO]: Digite algo no campo de texto");
        }

        int valor_personalizado = stringToInt(vp);
        if (valor_personalizado <= 0) {
            throw std::invalid_argument("\n[ERRO]: Digite apenas numeros inteiros validos\n");
        }


        if (static_cast<ModelosFrota>(modo) == ModelosFrota::CARRO) {
            veiculos.push_back(std::make_unique<Carro>(modelo, placa, valor_diaria, valor_personalizado));
            std::cout << "\n[SUCESSO]: Novo carro cadastrado\n";
        }
        if (static_cast<ModelosFrota>(modo) == ModelosFrota::MOTO) {
            veiculos.push_back(std::make_unique<Moto>(modelo, placa, valor_diaria, valor_personalizado));
            std::cout << "\n[SUCESSO]: Nova moto cadastrada\n";
        }

    }
    catch (const std::invalid_argument& e) {
        std::cout << "\n" << e.what() << "\n";
        return;
    }
}

void buscar_veiculo() {
    try {
        std::string placa_alvo, placa;
        std::cout << "Digite a placa do veiculo: ";
        std::getline(std::cin, placa_alvo);

        if (placa_alvo.empty()) {
            throw std::invalid_argument("[ERRO]: Digite algo no campo de texto");
        }

        for (const auto& p : veiculos) {
            placa = p->get_placa();

            if (placa_alvo == placa) {
                p->imprimir_status();
                return;
            }
        }
        throw std::invalid_argument("[ERRO]: Placa nao encontrada");
    }
    catch (const std::invalid_argument& e) {
        std::cout << "\n" << e.what() << "\n";
        return;
    }
}

void exibir_opcoes() {
    std::cout << "\n1. Simular aluguel da frota inteira\n"
              << "2. Cadastrar novo carro\n"
              << "3. Cadastrar nova moto\n"
              << "4. Buscar veiculo pela placa\n"
              << "0. Sair\n\n";
}

int main() {
    veiculos.push_back(std::make_unique<Carro>("Corola", "BHU-0935", 150, 4));
    veiculos.push_back(std::make_unique<Carro>("Ferrari", "FER-9393", 930, 2));
    veiculos.push_back(std::make_unique<Moto>("Tiger", "TIG-9373", 80, 800));
    veiculos.push_back(std::make_unique<Moto>("Panigale", "DUC-9393", 293, 1000));

    while (true) {
        try {
            exibir_opcoes();

            std::string entrada;
            std::cout << "Digite um numero: ";
            std::getline(std::cin, entrada);
            OpcaoAtual opcao = static_cast<OpcaoAtual>(stringToInt(entrada));

            switch(opcao) {
                case OpcaoAtual::SIMULAR_ALUGUEL:
                    simular_aluguel();
                    break;
                case OpcaoAtual::CADASTRAR_CARRO:
                    cadastrar_veiculo(1);
                    break;
                case OpcaoAtual::CADASTRAR_MOTO:
                    cadastrar_veiculo(2);
                    break;
                case OpcaoAtual::BUSCAR_VEICULO:
                    buscar_veiculo();
                    break;
                case OpcaoAtual::SAIR:
                    return 0;
                default:
                    throw std::invalid_argument("[ERRO]: Opcao inexistente no menu\n");
            }
        }
        catch (const std::invalid_argument& e) {
            std::cout << "\n" << e.what() << "\n";
            continue;
        }
    }
    return 0;
}