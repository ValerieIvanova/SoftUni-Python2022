lines = int(input())
longest_intersection = {}
for _ in range(lines):
    range1, range2 = input().split('-')
    start_idx1, end_idx1 = tuple(map(int, range1.split(',')))
    start_idx2, end_idx2 = tuple(map(int, range2.split(',')))
    set1 = {num for num in range(start_idx1, end_idx1+1)}
    set2 = {num for num in range(start_idx2, end_idx2+1)}
    intersection = set1 & set2
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
print(f"Longest intersection is [{', '.join(str(i) for i in longest_intersection)}] with length {len(longest_intersection)}")