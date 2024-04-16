def generate_candidate(prev_itemsets):
    candidate_itemset = []
    n = len(prev_itemsets)
    for i in range(n):
        for j in range(i + 1, n):
            itemset1 = prev_itemsets[i]
            itemset2 = prev_itemsets[j]
            if (itemset1[:-1] == itemset2[:-1]):
                candidate = sorted(list(set(itemset1) | set(itemset2)))
                candidate_itemset.append(candidate)
    return candidate_itemset


def generate_frequent(dataset, candidate_itemset, min_support):
    candidate_count = {}
    for transaction in dataset:
        for candidate in candidate_itemset:
            if set(candidate).issubset(set(transaction)):
                candidate_count.setdefault(tuple(candidate), 0)
                candidate_count[tuple(candidate)] += 1

    frequent_itemset = []
    for itemset, count in candidate_count.items():
        if (count >= min_support):
            frequent_itemset.append(list(itemset))

    return frequent_itemset


def apriori(database, min_support):
    item_count = max(max(transaction) for transaction in database)
    all_frequents = []
    candidate_itemset = [[item] for item in range(1, item_count + 1)]

    while candidate_itemset:
        frequent_itemset = generate_frequent(dataset=database, candidate_itemset=candidate_itemset,
                                             min_support=min_support)
        if frequent_itemset:
            all_frequents.extend(frequent_itemset)
        candidate_itemset = generate_candidate(prev_itemsets=frequent_itemset)

    return all_frequents


database = [[1, 2], [1], [2, 3], [1, 2, 3]]
min_support = 2

frequent_itemsets = apriori(database, min_support)

for frequent_items in frequent_itemsets:
    print(frequent_items)
