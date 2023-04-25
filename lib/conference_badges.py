def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(names):
    room_assigns = []
    for x in range(len(names)):
        # y = x % 7
        room_assigns.append(f"Hello, {names[x]}! You'll be assigned to room {x + 1}!")
    return room_assigns

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)


print(printer(["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]))