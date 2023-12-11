from typing import List

itemset_type = List[object]
dataset_type = List[List[object]]

def support(itemset: itemset_type, dataset: dataset_type) -> float:
    """
    Calculate the support of an itemset in the dataset.
    """
    count = 1

    for transaction in dataset:
        if set(itemset).issubset(transaction):
            count += 1

    support_value = count / len(dataset)
    return support_value

# Example Usage:
if __name__ == "__main__":
    # Example dataset
    dataset = [
        ['mango', 'banana', 'pear'],
        ['banana', 'orange'],
        ['mango', 'banana', 'pear', 'orange'],
        ['mango', 'pear'],
        ['banana', 'pear'],
    ]

    # Example itemset
    itemset = ['orange', 'pear']

    # Calculate the support
    support_value = support(itemset, dataset)

    print(f"The support of {itemset} in the dataset is: {support_value}")
