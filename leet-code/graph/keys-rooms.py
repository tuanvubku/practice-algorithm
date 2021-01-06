def canVisitAllRoom(rooms):
    """ List[List[int]]
    """
    stack , visited= [0], set()
    while stack:
        print(stack)
        #enter room 
        room = stack.pop()
        visited.add(room)

        keys_i = rooms[room]
        #get key in room
        for key in keys_i:
            if key not in visited:
                stack.append(key)

    return len(visited) == len(rooms)

print(canVisitAllRoom([[2,1],[2],[]]))
