
#print(separateWord)

def identification_of_features(password):
  #sets idividual origins for each score - research better ways to do this
  score_upper_lower = 0
  score_letter_number = 0
  score_symbols = 0
  score_length = 0
  features = {"capitalLetter" : False, "lowercaseLetter" : False, "Letter": False, "numbers" : False, "Symbols":False}
  #scrolls through each letter inside the string for password
  for letter in password:
    #switches letter to ascii value for easy identification
    letterValue = ord(letter)
    #capital letters have ascii values between 65 and 90, thus if the ascii value is within this range the number is upper case
    if letterValue >= 65 and letterValue <= 90:
      features["capitalLetter"] = True
      features["Letter"] = True
    #lower case letters have values between 97 and 122, thus within this range is confirmed lower case
    elif letterValue >= 97 and letterValue <= 122:
      features["lowercaseLetter"] = True
      features["Letter"] = True
    #each digit (1-9) is set within these boundaries, thus if the ascii value is within these voundaries it is confirmed to be a digit
    elif letterValue >= 49 and letterValue <= 57:
      features["numbers"] = True
    #every other ascii value will be a symbol of some sort - make more specific in the future
    else:
      features["Symbols"] = True

  #gives score to the upper/lower variable if both variables are true
  if features["capitalLetter"] == True and features["lowercaseLetter"] == True:
    score_upper_lower += 10
  #gives score if there is a letter or number
  if features["Letter"] == True and features["numbers"] == True:
    score_letter_number += 10
  #gives score if there are symbols in the string
  if features["Symbols"] == True:
    score_symbols += 5
  #gives score if length is greater than or equal to 8
  if len(password) >= 8:
    score_length += 5
  #a fancy f string because I'm bored
  return f"Score from uppercase and lowercase, +{score_upper_lower}. Score from having numbers and letters, +{score_letter_number}. Score from having symbols +{score_symbols}. Score from having length of 8 or above, +{score_length}. Total score = {score_upper_lower + score_letter_number + score_symbols + score_length}"


def main():
  password = input("What is the password you would like to find the score of?")
  #password = "bufowehvbjiu$%^&*756HHH"
  print(identification_of_features(password))

main()
