"""
Your job is to complete the definition of the function so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

def weather_helper():
  """
  Make suggestions based on current weather conditions.

  Program logic - indentations indicate nested logic:
  - Ask the user to enter in the current temperature in degrees Farenheit (i.e. an integer between  -70 and 134, inclusive).
    - If the user enters an invalid temperature (i.e. an integer that is not within the given range), print the text "Invalid temperature!" and do not print or input anything else.
    - If the temperature the user enters is below 40, ask them whether it is snowing.
      - If it is snowing, ask the user whether they are wearing a warm jacket.
        - If the user is wearing a jacket, print the output: "Glad to hear you're dressed appropriately!"
        - If the user is not wearing a jacket, print the output: "What were you thinking when you left home today?!"
      - If it is not snowing, ask the user whether it is raining.
        - If it is raining, ask the user whether they have an umbrella.
          - If the user has an umbrella, print the output: "Good job staying dry!"
          - If the user does not have an umbrella, print the output: "You must enjoy getting wet!"
    - If the temperature is above 90, ask the user whether they have air conditioning.
      - If the user has air conditioning, print the output: "Stay cool indoors."
      - If the user does not have air conditioning, print the output: "I hope you have a fan."

  Additional requirements:
    1. You can assume the user will enter an integer for the temperature.
    3. Assume the user will respond to any yes/no question with an affirmative response such as "yes", "yeah", "yup"; or a negative response such as "no", "nah", or "nope".
    2. Do not print anything more than what is requested in the instructions.
    4. The capitalization of the user's responses must not matter to the outcome of the program.
  """
  current_temperature = int(input("What is the current temperature? (between -70 and 134)"))
  if not(-70 <= current_temperature <= 134):
    print("Invalid temperature!")
  elif current_temperature < 40:
    is_it_snowing = input ("Is it snowing?").lower()
    if is_it_snowing == is_it_snowing == "yes" or is_it_snowing == "yeah" or is_it_snowing == "yup":
      are_you_wearing_a_jacket = input("Are you wearing a jacket?").lower()
      if are_you_wearing_a_jacket ==  are_you_wearing_a_jacket == "yes" or  are_you_wearing_a_jacket == "yeah" or  are_you_wearing_a_jacket == "yup":
        print("Glad to hear you're dressed appropriately!")
      elif are_you_wearing_a_jacket == "no" or are_you_wearing_a_jacket == "nah" or are_you_wearing_a_jacket == "nope":
        print("What were you thinking when you left home today?!")
    elif is_it_snowing == "no" or is_it_snowing == "nah" or is_it_snowing == "nope":
      is_it_raining = input("Is it raining?").lower()
      if is_it_raining == "yes" or is_it_raining == "yup" or is_it_raining == "yeah":
        do_you_have_an_umbrella = input("Do you have an umbrella?").lower()
        if do_you_have_an_umbrella == "yes" or do_you_have_an_umbrella == "yup" or do_you_have_an_umbrella == "yeah":
          print("Good job staying dry!")
        elif do_you_have_an_umbrella == "no" or do_you_have_an_umbrella == "nah" or do_you_have_an_umbrella == "nope":
          print("You must enjoy getting wet!")
      elif is_it_raining == "no" or is_it_raining == "nah" or is_it_raining == "nope":
        print()
  elif current_temperature > 90:
    do_you_have_air_conditioning = input("Do you have air conditioning?").lower()
    if do_you_have_air_conditioning == "yes" or do_you_have_air_conditioning == "yeah" or do_you_have_air_conditioning == "yup":
      print("Stay cool indoors.")
    elif do_you_have_air_conditioning == "no" or do_you_have_air_conditioning == "nah" or do_you_have_air_conditioning == "nope":
      print("I hope you have a fan.")