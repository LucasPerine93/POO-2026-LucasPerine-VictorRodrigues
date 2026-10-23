#include <iostream>
#include <iomanip>
#include <string>
#include <memory>
#include <stdexcept>
#include <vector>

class Aeroporto {
private:
    std::string nome, codigo_iata, status;
    std::vector<std::string> lista_voos, frota_avioes;

public:
    Aeroporto (std::string n, std::string cd, std::string st, std::vector<std::string> lv, std::vector<std::string> fa)
        : nome(n), codigo_iata(cd), status(st), lista_voos(lv), frota_avioes(fa) {}

    virtual ~Aeroporto() = default;

    bool validar_codigo(std::string codigo) {
        if (codigo.length() != 3) {
            std::invalid_argument("[ERRO]: Codigo invalido");
            return false;
        }

        return true;
    }

    void cadastrar_aviao(std::string aviao) {
        if (aviao.length() == 0) {
            std::invalid_argument("[ERRO]: Nome da aeronave nao preenchido");
        }

        frota_avioes.push_back(aviao);
    }

    void criar_voo(std::string voo) {

    }

    void buscar_voo(std::string) {

    }

    virtual void alterar_status(std::string novo_status) {

    }

    virtual void exibir_resumo() {

    }
};