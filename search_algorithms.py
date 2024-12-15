from collections import deque



## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    state_count = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True

    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state, action = search_queue.popleft()
        state_count += 1

        if goal_test(next_state):
            print("\n--- Breadth-First Search ---")
            print("Goal found")
            print(next_state)
            ptr = next_state
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            return next_state
        else :
            successors = next_state.successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)

    print("\n--- Breadth-First Search ---")
    print(F"Total states generated: {state_count}\n")
    return None

### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=0) :
    search_queue = deque()
    closed_list = {}
    state_count = 0

    search_queue.append((startState, "", 0))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state, action, depth = search_queue.pop()
        state_count += 1

        if goal_test(next_state):
            print("\n--- Depth-First Search ---")
            print("Goal found")
            print(next_state)
            ptr = next_state
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            return next_state
        elif depth < limit or limit == 0:
            successors = next_state.successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend([(s[0], s[1], depth + 1) for s in successors])

    print("\n--- Depth-First Search ---")
    print(F"Total states generated: {state_count}\n")
    return None
## add iterative deepening search here



#f
