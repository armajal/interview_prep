'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1+1"
Output: 2
Example 2:

Input: s = "6-4/2"
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

-----------------------------------
5:31pm
Input : expression string
Output : int of the value
Intuition:
        Use a stack for the order of operations

Approach
    stack = []
    open_brace = (
    close_brace = )
    operator_list = [+, -]
    priority_list = [* / ]
    res = 0 
    
    for char in string:
        if not open, close, or operator:
            push char unto stack
        
        if close operator:
            pop off stack until open

            stack_val = stack top 
            while stack and stack[-1] != open:
                stack_val += do_op(stack_val stack_top)
            
            do_op(stack_val, res, operation)

        if char is operation
            operation = char
            do_op (res, stack_top)

    do_op(left, right, operation)
        based on operation, does operation
        return val

'''