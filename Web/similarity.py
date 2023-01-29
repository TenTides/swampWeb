import pandas as pd

def compare(user1_list, comparison_df):
    classes = ["COP2500","COP3223C","CDA3103","COP3502C",
               "COP3503C","COP3330","COP3402","Foundation Exam",
               "COP4331C","COT3100","CIS3360"]
    
    group = []
    pref_dict = {}
    num_classes = {}
    overlap = {}
    likeness = {}
    most_alike = []
    
    user1_id = user1_list[0]
    user1_pref = int(user1_list[1])
    user1_classes = [classes[i] for i in range(len(classes)) if user1_list[i + 2] == 1]
    user1_num_classes = len(user1_classes)
    
    for index, row in comparison_df.iterrows():
        user2_list = list(row)
        user2_id = user2_list[0]
        user2_pref = int(user2_list[1])
        user2_classes = [classes[i] for i in range(len(classes)) if user2_list[i + 2] == "1"]
        user2_num_classes = len(user2_classes)
        
        overlapping_classes = [c for c in user1_classes if c in user2_classes]
        num_overlap = len(overlapping_classes)
        
        diff_classes = user1_num_classes + user2_num_classes - num_overlap
        similarity_score = float(num_overlap / diff_classes)
        
        if (len(overlapping_classes) > 0 and abs(user1_pref - user2_pref) <= 1 and similarity_score >= .5):
            pref_dict[user2_id] = user2_pref
            num_classes[user2_id] = user2_num_classes
            overlap[user2_id] = overlapping_classes
            likeness[user2_id] = similarity_score
    
    sorted_likeness = dict(sorted(likeness.items(), key=lambda item: item[1]))
                
    for key in sorted_likeness:
        most_alike.append(key)

    if (len(most_alike) == 0):
        return []
    
    group.append(user1_id)
    group.append(most_alike[0])
    
    group_size = min(user1_pref, pref_dict[most_alike[0]]);
    
    i = 1
    while (len(group) < group_size and i < len(most_alike)):
        curr = most_alike[i]
        if (abs(pref_dict[curr] - group_size) <= 1):
            group.append(curr)
        i += 1

    return group