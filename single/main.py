from collections import Counter


def build_counter(list_values):
    """
    Takes list and creates counter
    Args:
        list_values (list) list of objects
    Returns:
        cnt (Counter) dictionary of counts
    """
    cnt = Counter()
    for number in list_values:
        cnt[number] += 1
    return cnt


class Solution:

    def run(self, student_list):
        """
        Runs pipeline to find unpaired integers from student_list
        Args:
            student_list (list) list of objects
        Returns:
            (int) number with lowest count
        """
        cnt = build_counter(student_list)

        lowest_count = cnt.most_common()[-1]
        if lowest_count[1] == 1:
            return lowest_count[0]
        else:
            return "No single values"
