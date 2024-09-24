from mars_planner import (
    RoverState, move_to_sample, pick_up_tool, use_tool, move_to_station, mission_complete, goal_extract_sample
)
from search_algorithms import breadth_first_search, depth_first_search


def main():
    start_state = RoverState(loc="station", holding_tool=False, sample_extracted=False, holding_sample=False,
                             charged=False)

    action_list = [pick_up_tool, move_to_sample, use_tool, move_to_station]

    result = breadth_first_search(start_state, action_list, mission_complete)

    result2 = depth_first_search(start_state, action_list, mission_complete, use_closed_list=True, limit=5)


if __name__ == "__main__":
    main()




