class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz

    def recorrer(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        print("  " * nivel + f"Eval: {nodo.evaluacion}, MAX: {nodo.turno_max}")
        for hijo in nodo.hijos:
            self.recorrer(hijo, nivel + 1)



class Nodo:
    def __init__(self, estado, evaluacion=None, turno_max=True, jugada=None, padre=None):
        self.estado = estado              
        self.evaluacion = evaluacion      
        self.turno_max = turno_max        
        self.jugada = jugada              
        self.padre = padre                
        self.hijos = []                   

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


