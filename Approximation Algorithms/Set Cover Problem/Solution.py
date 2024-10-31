def set_cover_approx(universal, subsets):
    covered = set()
    selected_sets = []
    while covered !=universal:
        best_subset = max(subsets, key=lambda s: len(s-covered))
        selected_sets.append(best_subset)
        covered.update(best_subset)

    return selected_sets
subsets =[
    {1, 2, 3, 4, 5},
    {2, 3, 4, 5, 6},
    {3, 4, 5, 6, 7},
    {4, 5, 6, 7, 8},
    {5, 6, 7, 8, 9},

]

universal = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(set_cover_approx(universal, subsets))