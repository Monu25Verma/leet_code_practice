class Solution:
    def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:
        m = len(list1) + len(list2)
        list3 = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if (i + j) <= m:
                        if list3 == None:  # empty
                            list3.append(list2[j])

                        elif m == i + j:  # equal
                            list3.append(list2[j])

                        else:
                            list3 = []
                            list3.append(list2[j])

                        m = i + j
        return list3


print(Solution.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                              ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
