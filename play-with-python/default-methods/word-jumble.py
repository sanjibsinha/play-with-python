import random
import math

def word_jumble():
  """ 
  A word jumble game using various Python methods.
  """

  words = ["python", "programming", "language", "game", "puzzle"]
  word = random.choice(words) 
  jumbled_word = "".join(random.sample(word, len(word))) 

  print(f"Jumbled word: {jumbled_word}")

  attempts = 0
  max_attempts = math.ceil(math.log2(len(words)))  # Limit attempts based on word count

  while attempts < max_attempts:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == word:
      print(f"Congratulations! You guessed it in {attempts} attempts.")
      return

  print(f"Sorry, you ran out of attempts. The word was: {word}")

if __name__ == "__main__":
  word_jumble()