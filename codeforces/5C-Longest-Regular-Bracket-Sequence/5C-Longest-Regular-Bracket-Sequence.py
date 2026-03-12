#If there is a number
        while stack and isinstance(stack[-1], int):
            num += int(stack.pop()) 
        
        # Remove the opening bracket
        if stack and stack[-1] == '(':
            stack.pop()
            stack.append(num + 2)
        else:
            if num:
                stack.append(num)
            stack.append(ch)

    else:
        stack.append(ch)
        
# print(stack)
final_stack = []
for ch in stack:
    if isinstance(ch, int) and final_stack and isinstance(final_stack[-1], int):
        final_stack.append(ch + final_stack.pop())
    else:
        final_stack.append(ch)
# print(final_stack)
answer = list(filter(lambda x : isinstance(x, int), final_stack))
if answer:
    maxi = max(answer)
    count = (answer.count(maxi)) if maxi else 1

    print(maxi, count)
else:
    print(0, 1)