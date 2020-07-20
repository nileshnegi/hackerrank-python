"""
The Captain's Room

Mr. Anant Asankhya is the manager at the INFINITE hotel.
The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of ```K``` members per group

The Captain has a separate room, and the rest were given one room per group.
Mr. Anant has an unordered list of randomly arranged room entries.
The list consists of the room numbers for all of the tourists
which will appear ```K``` times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups is not known.
You only know the value of ```K``` and the room number list.
"""
if __name__ == "__main__":
    K = int(input())
    room_list = list(map(int, input().split()))
    rooms = dict()

    for i in range(len(room_list)):
        if rooms.get(room_list[i]) == None:
            rooms[room_list[i]] = 1
        else:
            rooms[room_list[i]] += 1
    
    for key, value in rooms.items():
        if value == 1:
            print(key)


"""
However this is a set problem. So the solution with sets:
"""
if __name__ == "__main__":
    K = int(input())
    rooms = map(int, input().split())

    single = set()
    multiple = set()

    for room in rooms:
        if room not in single:
            single.add(room)
        else:
            multiple.add(room)
    
    print(single.difference(multiple).pop())