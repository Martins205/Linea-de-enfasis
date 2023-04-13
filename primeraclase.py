class Node:
      def __init__(self, value):
          self.value = value #Raiz, el valor del nodo
          self.izquierda = None
          self.derecha = None
          
def preorden(node):
    if node is None:
       return
    print(node.value, end="  ")
    preorden(node.izquierda)
    preorden(node.derecha)
    
def postorden(node):
    if node is None:
       return    
    postorden(node.izquierda)
    postorden(node.derecha)
    print(node.value, end="  ")
    
def inorden(node):
    if node is None:
       return    
    inorden(node.izquierda)
    print(node.value, end="  ")
    inorden(node.derecha)
    

#Arbol
raiz = Node('A')
raiz.izquierda = Node('B')
raiz.derecha = Node('C')
raiz.izquierda.izquierda = Node('D')
raiz.izquierda.derecha = Node('E')
raiz.derecha.izquierda = Node('F')
raiz.derecha.derecha = Node('G')

print("Recorrido Preorden")
preorden(raiz)

print("\nRecorrido Postorden")
postorden(raiz)

print("\nRecorrido Inorden")
inorden(raiz)