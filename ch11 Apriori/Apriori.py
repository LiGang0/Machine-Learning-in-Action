# ====================================================================================
# Author: Junbo Xin
# Date: 2015/02/13-14
# Description:  Apriori Algorithm
# ====================================================================================

from numpy import *


# ================================= Part 1: find the frequent set =============================
def load_data_set():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


# giving data set, create a list that each element is an item of the set
def create_c1(data_set):
    c1 = []
    for transaction in data_set:
        for item in transaction:
            if not [item] in c1:  # ensure that c1 has unique items
                c1.append([item])
    c1.sort()
    return map(frozenset, c1)


# giving a data_set, and the candidate set ck, return the set in ck that satisfy mini support
def scan_d(data_set, ck, min_support):
    dic = {}
    for sets in data_set:
        for candidate in ck:
            if candidate.issubset(sets):
                if candidate in dic:
                    dic[candidate] += 1
                else:
                    dic[candidate] = 1

    num_items = float(len(data_set))
    return_list = []
    support_data = {}

    # go through each element in the dic
    for key in dic.keys():
        support = dic[key] / num_items
        if support >= min_support:
            return_list.insert(0, key)  # only satisfying mini support add in the list
        support_data[key] = support
    return return_list, support_data


# giving the set candidate and k, creates the set that each element has k elements
def generate_ck(candidate, k):
    ret_list = []
    m = len(candidate)
    for i in range(m):
        for j in range(i+1, m):
            l1 = list(candidate[i])[:k-2]
            l2 = list(candidate[j])[:k-2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                ret_list.append(candidate[i] | candidate[j])
    return ret_list


# obtain the ret_list as a list that contains l1, l2, l3..., support_data as a dict
def apriori(data_set, mini_support=0.5):
    # step 1: initialize c1 with 1-element set
    c1 = create_c1(data_set)
    all_set = map(set, data_set)

    # step 2: create in c1 that satisfy mini support
    l1, support_data = scan_d(all_set, c1, mini_support)
    ret_list = [l1]  # contains: l1, l2, l3,....
    k = 2

    # step 3: until  get k to the maximal
    while len(ret_list[k-2]) > 0:

        # step 4: giving (k-1)-elements set, generate k-elements set
        ck = generate_ck(ret_list[k-2], k)
        print '='*30, k, '='*30
        print ck

        # step 5:finds in ck that satisfy mini support
        lk, support_k = scan_d(all_set, ck, mini_support)
        support_data.update(support_k)
        ret_list.append(lk)
        k += 1
    return ret_list, support_data


# ============================== Part 2: Mining the Association Rules =========================
# @candidate_list: l1, l2, l3,...
# @support_data: dictionary, key is frequent set, value is support value
def generate_rules(candidate_list, support_data, min_confi=0.7):
    rule_list = []
    for i in range(1, len(candidate_list)):

        for freq_set in candidate_list[i]:
            # if {0,1,2}, h=[{0},{1},{2}]
            h = [frozenset([item]) for item in freq_set]

            # contains more than 1 elements
            if i > 1:
                pass
            else:
                pass
    return rule_list


def calc_conf(freq_set, h, support_data, rule_list, min_confi=0.7):
    rules = []
    for conseq in h:
        conf = support_data[freq_set] / support_data[freq_set-conseq]
        if conf >= min_confi:
            print freq_set-conseq, '-->', conseq, 'conf:', conf
            rule_list.append(freq_set-conseq, conseq, conf)
            rules.append(conseq)
    return rules

