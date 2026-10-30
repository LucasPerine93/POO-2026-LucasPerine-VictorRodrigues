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
    
    void set_pistas(std::vector<std::string>& pistas_cadastradas) {
        if (pistas_cadastradas.empty()) {
            throw std::invalid_argument("[ERRO]: Lista de pistas do aeroporto está vazia");
            return;
        }
        pistas_cadastradas = pistas;
    }

    virtual void set_status(std::string& status_operacao) {
        if (status_operacao.empty()) {
            throw std::invalid_argument("[ERRO]: Status vazio");
            return;
        }

        for (const auto& i : status_possiveis) {
            if (i == status_operacao) {
                std::cout << "[SUCESSO]: Status alterado com sucesso";
                status_operacao = status;
                return;
            }
        }

        throw std::invalid_argument("[ERRO]: Status invalido");
    }

    const std::vector<std::string>& get_pistas() {
        return pistas;
    }

    const std::string get_status() {
        return status;
    }

    virtual void exibir_resumo() {
        std::cout << "=== Dados do Aeroporto ===" << "\n"
          << "Nome: " << nome_aeroporto << "\n"
          << "Código ICAO: " << codigo_icao << "\n"
          << "Status: " << status << "\n"
          << "Localização: " << localizacao << "\n";
    }
};