# SOLUTION OF CODECHEF'S NAME REDUCTION PROBLEM ( DIFFICULTY RATING 1404 )

t = int(input())
for _ in range(t):
    a, b = input().split()
    n = int(input())
    children_name_combined = ""
    for i in range(n):
        children_name_combined += input()
    parents_name_combined = a+b
    var = True 
    for char in children_name_combined:
        if char in parents_name_combined:
            parents_name_combined = parents_name_combined.replace(char,"",1)
        else:
            var = False
    if var == True:
        print("YES")
    else:
        print("NO")

'''EXPLANATION - 
The code starts by taking an integer t as input, which likely represents the number of test cases to follow.

It enters a loop that iterates t times to process each test case.

For each test case, it takes two space-separated strings a and b as input, which are presumably the names of the parents.

It then takes an integer n as input, which probably represents the number of children's names to be checked in this test case.

Next, it initializes two empty strings: children_name_combined and parents_name_combined.

Within a nested loop that iterates n times, the code reads and appends child names to the children_name_combined string.

After gathering all child names, it combines the parent names into the parents_name_combined string.

The code initializes a boolean variable var to True, which will be used to determine whether it's possible to form all child names from the parent names.

It then iterates through each character in the children_name_combined string.

For each character, it checks if that character is present in the parents_name_combined string.

If the character is found in the parent names, it removes the first occurrence of that character from parents_name_combined.

If the character is not found in the parent names, it sets var to False.

After checking all characters, if var is still True, it means all child names can be formed from the parent names, so it prints "YES." Otherwise, it prints "NO."

In summary, the code takes multiple test cases, each with parent names and a list of child names. It checks if the parent names can be combined to form all the child names and prints "YES" or "NO" accordingly for each test case.'''
            
