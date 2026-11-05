#include <iostream>
#include <iomanip>
#include <string>
#include <memory>
#include <stdexcept>
#include <vector>

class Aeroporto {
private:
    // Aeroporto
    std::string nome_aeroporto, codigo_icao, status, localizacao;
    std::vector<std::string> pistas;
    std::vector<std::string> status_possiveis = {"Aberto", "Fechado", "Mayday", "Bloqueado"};
    

public:
    Aeroporto (std::string& p_nome_aeroporto, std::string& p_codigo_icao, std::string& p_status, std::string& p_localizacao)
        : nome_aeroporto(p_nome_aeroporto), 
          codigo_icao(p_codigo_icao), 
          status(p_status) {}

    virtual ~Aeroporto() = default;

    bool validar_codigo(std::string codigo) {

    }

    void cadastrar_aviao(std::string aviao) {

    }

    void criar_voo(std::string voo) {

    }

    void buscar_voo(std::string) {

    }

    virtual void alterar_status(std::string novo_status) {

    }

    virtual void exibir_resumo() {
        std::cout << "=== Dados do Aeroporto ===" << "\n"
          << "Nome: " << nome_aeroporto << "\n"
          << "Código ICAO: " << codigo_icao << "\n"
          << "Status: " << status << "\n"
          << "Localização: " << localizacao << "\n";
    }
};