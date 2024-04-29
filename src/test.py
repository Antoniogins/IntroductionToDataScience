# -------------------------------- #
# Exercise 1: read an integer from #
# console and compute an operation #
# with it                          #
# -------------------------------- #

# Cucumber


def operation(n):
    suma = 0
    for i in range(n + 1):
        suma += 4 * (-1) ** i / (2 * i + 1)
    return suma



# Cucumber

# Read the input coming from the console
print("Please, enter an integer number: ", end="")
n = int(input())

# Print the result
print(operation(n))
# Cucumber


# -------------------------------- #
# Exercise 2: to the previous      #
# exercise, add the code to return #
# -------------------------------- #
# the multiplication table of n    #
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# Cucumber
multiplication_table(n)


# -------------------------------- #
# Exercise 3: create a code that   #
# writes a tree-like form with the #
# numbers up to the introduced one #
# -------------------------------- #
print("Please, choose a number of rows to print: ", end="")
n = int(input())


def print_tree(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("\n")


# Cucumber
# Alternative
for i in range(1, n + 1):
    print(" ".join([str(f) for f in range(1, i)]))


print_tree(n)


# -------------------------------- #
# Exercise 4: ask for a number and #
# check whether the number is a    #
# prime number                     #
# -------------------------------- #
print("Please, introduce a number: ", end="")
n = int(input())


def is_prime(n):
    could_divide = False
    for i in range(2, n):  # remember range(a, b) creates a list from a to b-1
        if n % i == 0:
            could_divide = True
            break

    if could_divide:
        print("Number is not prime")
    else:
        print("Number is prime")


is_prime(n)


# -------------------------------- #
# Exercise 5: the same as before   #
# but just return True or False    #
# -------------------------------- #
def is_prime_true_or_false(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print("Please, introduce a number: ", end="")
n = int(input())
print(f"Number is prime: {is_prime_true_or_false(n)}")


# -------------------------------- #
# Exercise 6: write the code to    #
# return the prime numbers lower   #
# than a given number from console #
# -------------------------------- #
def print_primes(n):
    for i in range(1, n + 1):
        if is_prime_true_or_false(i):
            print(f"Prime number found: {i}")


print("Please, introduce a maximum number of tries to found primes: ", end="")
n = int(input())
print_primes(n)


# -------------------------------- #
# Exercise 7: make the challenge   #
# -------------------------------- #
personas = {"Pedro": 28, "María": 21, "Marta": 22}
esperanza_adicional = {28: 53.4, 21: 65.6, 22: 64.5}

esperanza_personas = {
    nombre: edad + esperanza_adicional[edad] for nombre, edad in personas.items()
}

print(f"Esperanza de vida de cada persona:\n{esperanza_personas}")
