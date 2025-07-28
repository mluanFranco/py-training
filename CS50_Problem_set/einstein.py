def formula(kilograms):
    e = kilograms * pow(300000000, 2)
    return e

def main():
    user_kg = int(input("m:"))
    print("E:", formula(user_kg))

main()
