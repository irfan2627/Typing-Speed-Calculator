import time
import enchant


def calculate_typing_speed(text, time_elapsed):
    d = enchant.Dict("en_US")
    words = text.split()
    num_words = len(words)
    num_correct_words = 0
    num_incorrect_words = 0

    for word in words:
        if d.check(word):
            num_correct_words += 1
        else:
            num_incorrect_words += 1

    speed = num_correct_words / (time_elapsed / 60)
    return speed, num_words, num_correct_words, num_incorrect_words


def typing_test():
    print("Welcome to the Typing Test!")
    print("Enter your text or Type the following text: 'The quick brown fox jumps over the lazy dog'")
    input("Press Enter when you're ready to start the timer.")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    time_elapsed = end_time - start_time
    speed, num_words, num_correct_words, num_incorrect_words = calculate_typing_speed(user_input, time_elapsed)
    print(f"\nYou typed {num_words} words with {num_incorrect_words} spelling mistakes and {num_correct_words} correctly.")
    print(f"Your typing speed is {speed:.2f} WPM.")
    return speed, num_words, num_correct_words, num_incorrect_words


results = typing_test()
print(results)
