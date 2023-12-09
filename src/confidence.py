dataset_type = list[list[object]]
rule_type = tuple[list[object], list[object]]

from typing import List, Tuple
def confidence(data_set: dataset_type, rule: rule_type) -> float:
    """
    To measure the likelihood of occurrence of an itemset given another itemset.
    """

    if premise_support == 0:
        return 0.0

    confidence_value = rule_support / premise_support
    return confidence_value

# Example Usage:

    # Example dataset
dataset = [
        ['apple', 'banana', 'cherry'],
        ['banana', 'orange'],
        ['apple', 'banana', 'cherry', 'orange'],
        ['apple', 'cherry'],
        ['banana', 'cherry'],
    ]

    # Example rule
rule = (['apple'], ['banana'])

    # Calculate confidence
confidence_value = confidence(dataset, rule)

print(f"The confidence of the rule {rule} in the dataset is: {confidence_value}")
