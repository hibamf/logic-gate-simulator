def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return int(not a)

def NAND(a, b):
    return int(not (a & b))

def NOR(a, b):
    return int(not (a | b))

def XOR(a, b):
    return a ^ b

print("🔌 Logic Gate Simulator 🔌")
print("Available gates: AND, OR, NOT, NAND, NOR, XOR")

while True:
    gate = input("\nEnter gate name (or 'exit' to quit): ").upper()
    
    if gate == "EXIT":
        break
    elif gate == "NOT":
        a = int(input("Enter input (0 or 1): "))
        print("Result:", NOT(a))
    elif gate in ["AND", "OR", "NAND", "NOR", "XOR"]:
        a = int(input("Enter first input (0 or 1): "))
        b = int(input("Enter second input (0 or 1): "))
        if gate == "AND":
            print("Result:", AND(a, b))
        elif gate == "OR":
            print("Result:", OR(a, b))
        elif gate == "NAND":
            print("Result:", NAND(a, b))
        elif gate == "NOR":
            print("Result:", NOR(a, b))
        elif gate == "XOR":
            print("Result:", XOR(a, b))
    else:
        print("Invalid gate. Please try again.")
