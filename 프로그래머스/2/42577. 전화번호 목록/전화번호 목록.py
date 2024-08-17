def solution(phone_book):
    answer = True
    phone_set = set()
    phone_book.sort()
    
    for num in phone_book:
        for i in range(len(num)):
            if num[:i+1] in phone_set:
                answer = False 
                return answer 
        phone_set.add(num)
    return answer