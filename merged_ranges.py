"""Write a function merge_ranges() that takes a list of multiple meeting time
ranges stored as tuple of integers and returns a list of condensed ranges.

For example, given: 
    [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

return:
    [(0, 1), (3, 8), (9, 12)]

Do not assum the meetings are in order.
"""

def merged_ranges(meetings):
    """given list of meeting times ranges, return a list of condensed ranges."""

    sorted_meetings = sorted(meetings)
    merged_meetings = [sorted_meetings[0]]

    for current_start_time, current_end_time in sorted_meetings[1:]:
        last_merged_start_time, last_merged_end_time = merged_meetings[-1]
        if current_start_time <= last_merged_end_time:
            merged_meetings[-1] = (last_merged_start_time, max(current_end_time, 
            last_merged_end_time))
        else:
            merged_meetings.append((current_start_time, current_end_time))
    return merged_meetings

print(merged_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(merged_ranges([(1, 2), (2, 3), (5, 8), (7, 9), (10, 12)]))