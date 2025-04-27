from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# Test outputs
print(Fore.RED + "This text is red.")
print(Fore.GREEN + "This text is green.")
print(Back.YELLOW + Fore.BLACK + "Black text on yellow background.")
print(Style.BRIGHT + "Bright text.")
print("Normal text again.")

