import random
def generate_random_character(n):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    random_character = ''.join(random.choice(characters) for _ in range(n))
    return random_character
n=int(input("Enter the length of the random character: "))
result = generate_random_character(n)
print("Generated random character:", result)