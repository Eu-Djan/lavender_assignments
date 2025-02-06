# Create a program that will:


# Store personal details (like name, age, and favorite colors) in variables and dictionaries.

name = input("what's your name: ")
age = input("How old are you? ")
fav_color = input("what's your favorite color? ")

user = {
    "name": name,
    "age": age,
    "favorite color" : fav_color,
}


# Store a list of friends' names.

friend_names = input("what are your friends' names?: ")
friend_names = friend_names.split(", ")
friend_names = list(friend_names)

print("These are your current details: ", user)

# Allow a user to update their personal information, like age and favorite color.e
changes = input("Do you want to make any changes? ").capitalize()

if changes == "Yes":

    new_name = input("whats your name?: ")
    user["name"] = new_name

    new_age = input("what's your age? ")
    user["age"] = new_age

    new_fav_color = input("what's your fav color?: ")
    user["favorite color"] = new_fav_color

else:
    print(user)
# Remove a friend from the list.
remove_friend = input("which friend do you want to remove: ")
if remove_friend in friend_names:
    friend_names.remove(remove_friend)
    print(f"{remove_friend} has been removed")
else:
    print("Name not found")

# Display the updated information in an organized format.
print("These are your updated details: ", user)

print("And these are your friends' names: ", friend_names)




