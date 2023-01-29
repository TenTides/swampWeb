import pandas as pd

def compare(user1_list, comparison_df):
    classes = ["COP2500","COP3223C","CDA3103","COP3502C",
               "COP3503C","COP3330","COP3402","Foundation Exam",
               "COP4331C","COT3100","CIS3360"]
    
    match_dict = {}
    could_be_match = 0
    user1_id = user1_list[0]
    user1_hosting = (user1_list[1] == "Yes")
    user1_classes = [classes[i] for i in range(len(classes)) if user1_list[i + 2] == 1]
    user1_num_classes = len(user1_classes)
    
    for index, row in comparison_df.iterrows():
        user2_list = list(row)
        user2_id = user2_list[0]
        user2_hosting = (user2_list[1] == "Yes")
        user2_classes = [classes[i] for i in range(len(classes)) if user2_list[i + 2] == "1"]
        user2_num_classes = len(user2_classes)
        
        overlapping_classes = [c for c in user1_classes if c in user2_classes]
        if (len(overlapping_classes) > 0):
            if (user1_hosting == user2_hosting):
                could_be_match += 1
            else:
                match_dict[user2_id] = [user2_num_classes] + overlapping_classes
                    
    return match_dict
