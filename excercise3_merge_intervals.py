def merge_ranges(intervals):

    if not intervals:
        return []

    intervals.sort()

    result = []
    temp = intervals[0]

    for item in intervals[1:]:

        if item[0] <= temp[1]:
            temp[1] = max(temp[1], item[1])
        else:
            result.append(temp)
            temp = item

    result.append(temp)

    return result


nums = [[1,3], [2,6], [8,10]]
print(merge_ranges(nums))
