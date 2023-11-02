# Classe para representar um caminhão
class Caminhao:
    def __init__(self, placa, localizacao):
        self.placa = placa
        self.localizacao = localizacao
        self.pneus = {"dianteiro_esquerdo": 100, "dianteiro_direito": 100, "traseiro_esquerdo": 100, "traseiro_direito": 100}
        self.nivel_oleo = 100

    def verificar_pneus(self):
        for pneu, pressao in self.pneus.items():
            if pressao < 30:
                print(f"Pneu {pneu} com pressão baixa. Troque o pneu.")
            else:
                print(f"Pneu {pneu} com pressão adequada.")

    def verificar_oleo(self):
        if self.nivel_oleo < 20:
            print("Nível de óleo baixo. Faça a troca de óleo imediatamente.")
        else:
            print("Nível de óleo adequado.")

    def realizar_troca_pneu(self):
        print("Realizando troca de pneu...")
        # Lógica para a troca de pneu
        self.pneus = {"dianteiro_esquerdo": 100, "dianteiro_direito": 100, "traseiro_esquerdo": 100, "traseiro_direito": 100}
        print("Troca de pneu concluída.")

    def realizar_troca_oleo(self):
        print("Realizando troca de óleo...")
        # Lógica para a troca de óleo
        self.nivel_oleo = 100
        print("Troca de óleo concluída.")

    def atualizar_localizacao(self, nova_localizacao):
        self.localizacao = nova_localizacao
        print(f"Localização atualizada para {nova_localizacao}.")

# Exemplo de uso
caminhao1 = Caminhao("ABC123", "Fazenda A")
caminhao1.verificar_pneus()
caminhao1.verificar_oleo()

# Simulando uma troca de pneu
caminhao1.realizar_troca_pneu()
caminhao1.verificar_pneus()

# Simulando uma troca de óleo
caminhao1.realizar_troca_oleo()
caminhao1.verificar_oleo()

# Atualizando a localização do caminhão
caminhao1.atualizar_localizacao("Fazenda B")