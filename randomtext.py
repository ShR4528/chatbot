import time
import random
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama


def generate_random_code():
    codes = [
        'console.log("Hello, world!");',
        'function factorial(n) { return n <= 1 ? 1 : n * factorial(n-1); }',
        'const arr = [1, 2, 3, 4, 5]; arr.forEach(item => console.log(item));',
        'const sum = (a, b) => a + b;',
        'for (let i = 0; i < 10; i++) { console.log(i); }',
    ]
    return random.choice(codes)


def typing_trainer(code):
    print(Fore.GREEN + "Type the following JavaScript code:")
    print(code)
    print(Style.RESET_ALL)

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    # Calculate typing speed and accuracy
    total_time = end_time - start_time
    code_length = len(code)
    correct_chars = sum([1 for i in range(
        min(len(user_input), code_length)) if user_input[i] == code[i]])
    accuracy = (correct_chars / code_length) * 100

    # Calculate typing speed in characters per second (CPS) and words per minute (WPM)
    cps = code_length / total_time
    wpm = cps * 60 / 5  # Assuming an average word has 5 characters

    print(Fore.BLUE + "\nResults:")
    print(f"Elapsed time: {total_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Characters per second (CPS): {cps:.2f}")
    print(f"Words per minute (WPM): {wpm:.2f}")
    print(Style.RESET_ALL)


if __name__ == "__main__":
    print(Fore.YELLOW + "Welcome to the JavaScript typing trainer!")
    print(Style.RESET_ALL)

    while True:
        random_code = generate_random_code()
        typing_trainer(random_code)

        print(Fore.YELLOW + "Do you want to repeat the practice? (y/n)")
        print(Style.RESET_ALL)

        repeat = input().lower()
        if repeat != 'y':
            break
