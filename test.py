from pyjokes import get_joke
from emoji import emojize
from random_profile import RandomProfile

if __name__ == "__main__":
    print(RandomProfile().full_name()[0], end=":\n")
    print(emojize(':speech_balloon:'), end=" ")
    print(get_joke(), end=" ")
    print(emojize(':speech_balloon:'))