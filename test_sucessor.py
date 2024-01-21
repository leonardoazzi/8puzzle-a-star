from gameLogic import sucessor

def test_sucessor():
    assert sucessor("2_3541687") == {('abaixo', '2435_1687'), ('esquerda', '_23541687'), ('direita', '23_541687')}

if __name__ == "__main__":
    test_sucessor()
    print("Todos os testes passam.")