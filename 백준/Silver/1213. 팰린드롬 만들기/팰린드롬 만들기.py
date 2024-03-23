from collections import Counter

def palindrome(word):
    answer = ""
    word = Counter(word)
    word_set = list(word.keys())
    word_set.sort()
    word_odd = [w for w in word_set if word[w]%2!=0]

    for w in word_set:
        answer += w*(word[w]//2)

    if word_odd:
        answer = answer + word_odd[0] + answer[::-1]
    else:
        answer = answer + answer[::-1]

    return str(''.join(answer))


n = input()
counter_n = Counter(n)
check_odd = [1 if i%2!=0 else 0 for i in counter_n.values()]
if (len(n)%2==0 and sum(check_odd)==0) or\
    (len(n)%2!=0 and sum(check_odd)==1):
    print(palindrome(n))

else:
    print("I'm Sorry Hansoo")
