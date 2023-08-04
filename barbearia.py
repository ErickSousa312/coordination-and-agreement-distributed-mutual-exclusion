import threading
import time

class Barbeiro:
    def __init__(self):
        self.mutex = threading.Lock()

    def cortarCabelo(self, cliente_num):
        print(f"Barbeiro: Cliente {cliente_num}, cortando cabelo...")
        time.sleep(3)
        print(f"Barbeiro: Cabelo do Cliente {cliente_num} cortado!")

    def cortarBarba(self, cliente_num):
        print(f"Barbeiro: Cliente {cliente_num}, cortando barba...")
        time.sleep(4)
        print(f"Barbeiro: Barba do Cliente {cliente_num} cortada!")

    def cortarBigode(self, cliente_num):
        print(f"Barbeiro: Cliente {cliente_num}, cortando bigode...")
        time.sleep(5)
        print(f"Barbeiro: Bigode do Cliente {cliente_num} cortado!")

class ExclusaoMutua:
    def __init__(self):
        self.mutex = threading.Lock()
        self.barbeiro = Barbeiro()
        self.clienteNumero = 0
        self.servicos = ["cabelo", "barba", "bigode"]
        self.atendimento_disponivel = {
            "cabelo": threading.Lock(),
            "barba": threading.Lock(),
            "bigode": threading.Lock(),
        }

    def cliente(self, servico):
        self.mutex.acquire()
        self.clienteNumero += 1
        cliente_num = self.clienteNumero
        self.mutex.release()

        print(f"Cliente {cliente_num}: Quero cortar {servico}")

            # Espera até que o serviço esteja disponível
        with self.atendimento_disponivel[servico]:
            if servico == "cabelo":
                self.barbeiro.cortarCabelo(cliente_num)
            elif servico == "barba":
                self.barbeiro.cortarBarba(cliente_num)
            elif servico == "bigode":
                self.barbeiro.cortarBigode(cliente_num)

if __name__ == "__main__":
    exclusao_mutua = ExclusaoMutua()

    clientes = [
        threading.Thread(target=exclusao_mutua.cliente, args=("cabelo",)),
        threading.Thread(target=exclusao_mutua.cliente, args=("cabelo",)),
        threading.Thread(target=exclusao_mutua.cliente, args=("barba",)),
        threading.Thread(target=exclusao_mutua.cliente, args=("bigode",)),
        threading.Thread(target=exclusao_mutua.cliente, args=("barba",)),
        threading.Thread(target=exclusao_mutua.cliente, args=("bigode",)),
        
        
    ]

    for cliente in clientes:
        cliente.start()

    for cliente in clientes:
        cliente.join()
