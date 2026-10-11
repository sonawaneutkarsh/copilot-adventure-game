#!/usr/bin/env python3


def get_choice(options):
    while True:
        choice = input("\nEnter your choice number: ").strip()
        if choice in options:
            return choice
        print("Invalid choice. Please enter one of:", ", ".join(options))


def entrance(state):
    print("\nMidnight rain drums against the stained glass as you step into Ravenmoor Library.")
    print("Shadows stretch between towering shelves, and a clock ticks thirteen.")
    print("1) Slip into the reading room")
    print("2) Descend the creaking stairs to the basement")

    choice = get_choice({"1", "2"})
    if choice == "1":
        return "reading_room"
    return "basement_ending"


def reading_room(state):
    print("\nDusty chandeliers sway above rows of mahogany tables.")
    print("A whisper curls through the stacks: 'Find the archive before it finds you.'")
    print("1) Search the reference desk")
    print("2) Climb the iron stairs to the balcony")
    print("3) Run for the front doors")

    choice = get_choice({"1", "2", "3"})
    if choice == "1":
        return "reference_desk"
    if choice == "2":
        return "balcony"
    return "front_doors"


def reference_desk(state):
    print("\nYou open warped drawers in the reference desk.")
    if "brass key" not in state["inventory"]:
        print("Inside a velvet pouch, you find a cold brass key and pocket it.")
        state["inventory"].add("brass key")
    else:
        print("The drawers are empty now, save for splinters and dust.")
    print("1) Return to the reading room")
    print("2) Follow a draft toward the archive corridor")

    choice = get_choice({"1", "2"})
    if choice == "1":
        return "reading_room"
    return "archive_door"


def balcony(state):
    print("\nFrom the balcony, you see pale figures gliding between shelves below.")
    print("The whisper returns, stronger now, from the dark archive corridor.")
    print("1) Follow the whisper toward the archive")
    print("2) Lean over the railing for a better look")

    choice = get_choice({"1", "2"})
    if choice == "1":
        return "archive_door"
    return "wraith_ending"


def front_doors(state):
    print("\nYou reach the carved oak doors, but iron chains bind them from the outside.")
    print("A cold laugh echoes behind you in the entry hall.")
    print("1) Pull the chains with all your strength")
    print("2) Retreat and search for another way out")

    choice = get_choice({"1", "2"})
    if choice == "1":
        return "trapped_ending"
    return "archive_door"


def archive_door(state):
    print("\nAt the end of the corridor stands the archive room: a steel door with a keyhole.")
    if "brass key" in state["inventory"]:
        print("The brass key in your pocket hums with warmth.")
    else:
        print("The lock is old, intricate, and impossible to pick by hand.")
    print("1) Try to unlock the archive room")
    print("2) Retreat to the reading room")

    choice = get_choice({"1", "2"})
    if choice == "2":
        return "reading_room"

    if "brass key" in state["inventory"]:
        return "archive_escape_ending"

    print("\nYou rattle the handle, but the sealed door does not move.")
    print("You need a brass key.")
    return "archive_door"


def basement_ending(state):
    print("\nThe basement lights flicker on, revealing a circle of open books on the floor.")
    print("Before you can run, the pages whip into a storm and swallow your scream.")
    print("\nGAME OVER: The library keeps you forever.")
    return None


def wraith_ending(state):
    print("\nYou lean over the railing as unseen hands grip your shoulders.")
    print("The last thing you hear is the scrape of your own shoes across rusted iron.")
    print("\nGAME OVER: The watchers in the stacks claim another reader.")
    return None


def trapped_ending(state):
    print("\nThe chains snap tight around your wrists like living serpents.")
    print("Footsteps gather in the dark behind you, then stop at your back.")
    print("\nGAME OVER: Midnight never ends inside Ravenmoor.")
    return None


def archive_escape_ending(state):
    print("\nThe brass key turns. The archive door opens to a hidden passage lit by moonlight.")
    print("You sprint through the tunnel and emerge outside as the first bell of dawn rings.")
    print("\nVICTORY: You escape the haunted library with your sanity intact.")
    return None


def main():
    print("Welcome to Midnight at Ravenmoor Library")
    print("Make your choices carefully. Some doors should stay closed.")

    state = {"inventory": set()}
    current_scene = "entrance"

    scenes = {
        "entrance": entrance,
        "reading_room": reading_room,
        "reference_desk": reference_desk,
        "balcony": balcony,
        "front_doors": front_doors,
        "archive_door": archive_door,
        "basement_ending": basement_ending,
        "wraith_ending": wraith_ending,
        "trapped_ending": trapped_ending,
        "archive_escape_ending": archive_escape_ending,
    }

    while current_scene is not None:
        current_scene = scenes[current_scene](state)


if __name__ == "__main__":
    main()
