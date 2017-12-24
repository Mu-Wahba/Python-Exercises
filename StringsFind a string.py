def count_substring(string, sub_string): #abcdcdc   cdc
    count=0
    for i in range (string.find(sub_string),len(string)):
        if string[i]==sub_string[0]:
            if string[i+1:i+len(sub_string)]==sub_string[1:]:
                count =count + 1
    return count
