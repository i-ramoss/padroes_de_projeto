from src import Guerreiro, LutaArco, LutaEspada, Curar

cavaleiro = Guerreiro(LutaEspada(8))
arqueiro = Guerreiro(LutaArco(6))
curandeiro = Guerreiro(Curar(5))


cavaleiro.acao()
arqueiro.acao()
curandeiro.acao()
