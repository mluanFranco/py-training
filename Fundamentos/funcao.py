# criacao de uma funcao
def hello(to="world"):  # valor padrao world
    print(f"Hello {to}, it is nice to finally meet you!")

hello()
name = input("What's your name? ")
hello(name)

# funcao ao quadrado
def main():
    x = int(input("Whats X?: "))
    print(f"{x} squared is {square(x)}")

def square(n):
    return pow(n,2) # power of (elevado)

main()