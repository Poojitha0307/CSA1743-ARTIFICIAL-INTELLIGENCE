from collections import deque

goal_state = '123456780'  # 0 represents blank
moves = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[4,6,8],8:[5,7]}

def bfs(start):
    visited = set()
    queue = deque([(start, [])])
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        visited.add(state)
        zero = state.index('0')
        for move in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = ''.join(new_state)
            if new_state not in visited:
                queue.append((new_state, path + [state]))
    return None

start_state = "125340678"  # Example initial state
solution = bfs(start_state)
for step in solution:
    print(step[0:3], "\n", step[3:6], "\n", step[6:9], "\n")
