from typing import Counter
from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(number):
    new_fact_list = []
    count = 0
    while len(new_fact_list) < number and count < 1000:
        koala_fact = random_koala_fact()
        count = count + 1
        if koala_fact not in new_fact_list:
            new_fact_list.append(koala_fact)
        else:
            continue
    return new_fact_list


def num_joey_facts():
    joeys_list = []
    found_same_fact = []
    while len(found_same_fact) < 10:
        koala_fact = random_koala_fact()
        if "joey" in str(koala_fact):
            if koala_fact not in joeys_list:
                joeys_list.append(koala_fact)
            elif found_same_fact == [] or koala_fact in found_same_fact:
                found_same_fact.append(koala_fact)
        else:
            continue
    return len(joeys_list)


def koala_weight():
    weight_fact = []
    while len(weight_fact) < 1:
        koala_fact = random_koala_fact()
        if "kg" in str(koala_fact):
            weight_fact.append(koala_fact)
        else:
            continue

    weight_fact_str = ""
    weight_fact_str = weight_fact_str.join(weight_fact)
    for word in weight_fact_str.split():
        if word.isdigit():
            return word
    weight_in_kg = "".join(filter(str.isdigit, word))
    return int(weight_in_kg)


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    random_koala_fact()
    unique_koala_facts(20)
    num_joey_facts()
    koala_weight()
