'''
exc_type: O tipo exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

exc_val: O valor da exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

exc_tb: O traceback (rastreamento de pilha) associado à exceção que ocorreu,
se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None
'''

class AlgumaCoisa:
    def __enter__(self):
        print("estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("estou saindo")

with AlgumaCoisa() as something:
    print("estou no meio")
