
def get_vowel_num(s):
    count = 0
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in vowel_list:
            count += 1
    return count

