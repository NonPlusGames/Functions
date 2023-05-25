# FUNCTIONS -----------------------------------------------------------------------------
# def function_name(parameters, separated, by, commas):
#   internal_code
#   return return_value
# output = function_call(arguments, separated, by, commas)


# DEFINE the function
def shout(name):
  name = name.upper()
  return "HELLO " + name + "!"

# CALL the function (use it)
shouted_name = shout("Jeremy") # Store the return of this function call in a variable
print(shouted_name) # Print the return of the function call

# # Functions with multiple parameters ---------------------
# # Define the function
# def personalized_age_check(name, age):
#   if age >= 18:
#     return "Congratulations " + name + "! You're old enough to vote."
#   else:
#     time_left = 18 - age
#     return "Sorry, " + name + ". You can't vote for another " + str(time_left) + " years."

# # Call the function
# print(personalized_age_check("Jeff", 28))
# print(personalized_age_check("Zara", 14))

# # Functions with no arguments ---------------------
# def pi_reminder():
#   return 3.14159265358979

# # Functions with no return ---------------------
# def add(x, y):
#   total = x + y

# # Call
# print(add(5, 22))

# # Returns as break points ---------------------
# # Defenition
# def add(x, y):
#   print("Adding your numbers")
#   total = x + y
#   return total
#   print("Finished adding")

# # Call
# print(add(5, 22))

# # LAB TIME (Activity Planner *) (Budget Buddy * *) --------------------------------------------------------

# # Calling with variables ---------------------
# def greet(player):
#   if player == "Octavia":
#     return "Welcome, agent Spencer. We're big fans."
#   else:
#     return "Welcome, " + player

# # Use a variable to collect and store user input
# name1 = input("Enter player 1's name")

# # Pass in our `name1` variable as the argument for our greet function.
# print(greet(name1))

# name2 = input("Enter player 2's name")
# print(greet(name2))

# # Default parameters ---------------------
# def greet_player(name = "User"):
#   print("Welcome to the game, " + name + ".")
#   print("Your current level is 1.")

# greet_player("David") # Code if the user provides their name
# greet_player()  # Code if the user chooses not to provide their name

# # Scope ---------------------
# age = 15

# def have_a_birthday():
# #   global age
#   age = 20
#   age += 1
#   print("Happy birthday! You're now " + str(age))
#   return age

# have_a_birthday()

# print(age)

# # LAB TIME --------------------------------------------------------
# (Super Mario Stairs *) - Create the stairs with a height set by the user
# (Investment Functions * *) 