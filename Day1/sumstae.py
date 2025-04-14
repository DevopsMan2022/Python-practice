def sum_state(a: int,b: int)-> int:
    """
    This function will take 2 numbers as input 
    1. a int
    2. b int
    and will print the output as positive , negitive or zero
    """
    c = a+b
    if (c>0):
        state = 'positive'
    elif(c<0):
        state = 'Negative'
    else:
        state = 'zero'
    return state