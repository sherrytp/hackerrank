# https://www.hackerrank.com/challenges/the-time-in-words/problem

num_dict=  {0: 'zero',
 1: 'one',
 2: 'two',
 3: 'three',
 4: 'four',
 5: 'five',
 6: 'six',
 7: 'seven',
 8: 'eight',
 9: 'nine',
 10: 'ten',
 11: 'eleven',
 12: 'twelve',
 13: 'thirteen',
 14: 'fourteen',
 15: 'fifteen',
 16: 'sixteen',
 17: 'seventeen',
 18: 'eighteen',
 19: 'nineteen',
 20: 'twenty',
 21: 'twenty one',
 22: 'twenty two',
 23: 'twenty three',
 24: 'twenty four',
 25: 'twenty five',
 26: 'twenty six',
 27: 'twenty seven',
 28: 'twenty eight',
 29: 'twenty nine'}
 
# Complete the timeInWords function below.
def timeInWords(h, m, num_dict):
    if m==0:
        return f"{num_dict[h]} o' clock"
    elif m==15:
        return f"quarter past {num_dict[h]}"
    elif m==45:
        return f"quarter to {num_dict[h+1]}"
    elif m==30:
        return f"half past {num_dict[h]}"
    elif m<30:
        if m>1:
            return f"{num_dict[m]} minutes past {num_dict[h]}"
        else:
            return f"{num_dict[m]} minute past {num_dict[h]}"
    elif m>30 and 60-m>1:
        return f"{num_dict[60-m]} minutes to {num_dict[h+1]}"
    elif m>30 and 60-m==1:
        return f"{num_dict[60-m]} minute to {num_dict[h+1]}"
    else:
        return f"{num_dict[m]} minutes past {num_dict[h]}"
    