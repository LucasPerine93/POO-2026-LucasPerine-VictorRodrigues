#include <iomanip>
#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
#include <cstdint>

class Voo {
private:
    std::string codigo, origem, destino, data, horario, status;
    uint16_t assentos_disponiveis;

public:
    Voo (std::string cd, std::string org, std::string dst, std::string dt, std::string hr, std::string st, uint16_t asd)
        : codigo(cd), origem(org), destino(dst), data(dt), horario(hr), status(st), assentos_disponiveis(asd) {}
    
    virtual ~Voo() = default; 

    void cadastrar() {}
    void designar_aeronave() {}
    bool reservar_assento() {}
    void liberar_assento() {}
    void atrasar() {}
    void cancelar() {}
    std::vector<uint16_t> listar_passageiros() {}

};

int main() {
    return 0;
}