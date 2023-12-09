ourcetemset_type = list[object]
dataset_type = list[list[object]]


def support(itemsets: dataset_type, data_set: itemset_type) -> float:
    """
    To find the frequency of itemsets in the dataset.
    """
    from typing import List
dataset = [
            ['apple', 'banana', 'cherry'],
            ['banana', 'orange'],
            ['apple', 'banana', 'cherry', 'orange'],
            ['apple', 'cherry'],
            ['banana', 'cherry'],
            ]

            # Example itemset
itemset = ['apple', 'banana']

            # Calculate the support
support_value = support(itemset, dataset)
