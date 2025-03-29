def process_cards(num_of_rounds):
    cards = input("Enter a string of cards separated by space: ").split()
    for _ in range(num_of_rounds):
        m = int(input())
        h = int(input()) - 1 # subracting one to index from 0-based system
        print(' '.join(cards[h::len(cards)]))
        
# Example usage: process_cards(3)
# Input:
# Enter a string of cards separated by space: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# 4
# 5
# 0
# 6
# Output:
# A C G M P
# 
# Input:
# Enter a string of cards separated by space: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# 7
# 5
# 0
# Output:
# A B D G J 

# Input:
# Enter a string of cards separated by space: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# 10
# 7
# 3
# Output:
# A D G J K M P 

# Input:
# Enter a string of cards separated by space: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# 13
# 9
# 7
# Output:
# C F J L S X 
```python
def process_cards(num_of_rounds):
    cards = input("Enter a string of cards separated by space: ").split()
    for i in range(num_of_rounds):
        m = int(input()) - 1 # subracting one to index from 0-based system
        h = int(input()) - 1 # subracting one to index from 0-based system
        print(' '.join(cards[h::len(cards)]))
```