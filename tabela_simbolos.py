class TabelaSimbolos:
    def __init__(self):
        self.pilha_escopos = [{}]

    def entrar_escopo(self):
        self.pilha_escopos.append({})

    def sair_escopo(self):
        if len(self.pilha_escopos) > 1:
            self.pilha_escopos.pop()

    def declarar(self, variavel, tipo):
        escopo_atual = self.pilha_escopos[-1]
        if variavel in escopo_atual:
            return False
        escopo_atual[variavel] = tipo
        return True

    def buscar(self, variavel):
        for escopo in reversed(self.pilha_escopos):
            if variavel in escopo:
                return escopo[variavel]
        return None

if __name__ == "__main__":
    ts = TabelaSimbolos()

    print("=== Teste 1: Escopo Global ===")
    ts.declarar("x", "int")
    ts.declarar("y", "float")
    print("Busca 'x':", ts.buscar("x"))
    print("Busca 'y':", ts.buscar("y"))

    print("\n=== Teste 2: Novo Escopo (Local) ===")
    ts.entrar_escopo()
    ts.declarar("z", "string")
    ts.declarar("x", "boolean")
    print("Busca 'z' (local):", ts.buscar("z"))
    print("Busca 'x' (shadowing):", ts.buscar("x"))
    print("Busca 'y' (herdado):", ts.buscar("y"))

    print("\n=== Teste 3: Conflito no Mesmo Escopo ===")
    sucesso = ts.declarar("z", "int")
    print("Tentar redeclarar 'z' no mesmo escopo:", sucesso)

    print("\n=== Teste 4: Saindo do Escopo ===")
    ts.sair_escopo()
    print("Busca 'z' apos sair do escopo:", ts.buscar("z"))
    print("Busca 'x' apos sair do escopo:", ts.buscar("x"))