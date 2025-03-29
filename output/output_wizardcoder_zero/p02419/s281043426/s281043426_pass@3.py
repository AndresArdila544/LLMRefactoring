def count_word(W):
    T = input()
    count = 0
    
    for line in sys.stdin:
        target = line.strip().lower()
        
        if target == "END_OF_TEXT":
            break
        
        if W.lower() == target:
            count += 1
            
    print(count)