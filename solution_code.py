guests = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

def remove_guest(guest_name, response):
  """
  Removes a guest from the list if they responded 'no' to the party invitation.

  Arguments:
    guest_name: The name of the guest to remove from the list
    response: The guest's response to the invitation ('yes' or 'no').
  """
  try:
    guest_index = guests.index(guest_name)
    if response.lower() in ['no', 'n']:
      guests.pop(guest_index)
      print(f"{guest_name} RSVP'd no and has been removed from the guest list.")
  except ValueError:
    print(f"Sorry! {guest_name} was not found in the guest list.")

remove_guest("Bob", "No")
remove_guest("Alice", "Yes")
remove_guest("Charlie", "no")

print(f"Updated guest list: {guests}")
