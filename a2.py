name = input("Enter your real name, Agent: ")
gadget = input("Enter your favorite gadget: ")
# PART 2: Store the agent's details using different data types
agent_number=7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True
# PART 3: Print each detail along with its data type
print("Name:", name, "-> type:", type(name))
print("Gadget:", gadget, "-> type:", type(gadget))
print("Agent Number:", agent_number, "-> type:", type(agent_number))
print("Speed Rating:", speed_rating, "-> type:", type(speed_rating))
print("Mission Count:", mission_count, "-> type:", type(mission_count))
print("Height (m):", height_m, "-> type:", type(height_m))
print("Is Active:", is_active, "-> type:", type(is_active))
# PART 4: Typecast the numbers and true/false value into text
agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)
print("Agent Number as text:", agent_number_text, "-> type:", type(agent_number_text))
print("Mission Count as text:", mission_count_text, "-> type:", type(mission_count_text))
print("Speed Rating as text:", speed_rating_text, "-> type:", type(speed_rating_text))
print("Status as text:", status_text, "-> type:", type(status_text))
first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Secret Code Name:", code_name)