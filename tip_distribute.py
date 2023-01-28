from art import logo

#Much better, need to create a dictionary "workers{}" that takes name as key and sum of tips from EMP_LIST as value

EMP_LIST = []
SHIFT = 0
EMP_NUM = 0

print(logo)
print("This is a 'very' simple tip distribution calculator.\nTips are first distributed into shifts.\nThen evenly across number of employees who worked that shift.\n\n")


#Find names for shifts
def names():
    return input("Enter names her followed by spaces:\nEx. 'John, Beth, Sarah'\n\n: ").lower().split(", ")

def tips():
    return float(input("Total at end of shift:\n\n$"))

def shifts(n):
    global EMP_LIST
    EMP_LIST.append({
        "Shift": n,
        "Tip Total": tips(),
        "Workers": names(),
    })
    
def distips():
    global EMP_LIST
    tip_dist = EMP_LIST[SHIFT]["Tip Total"] / EMP_NUM
    EMP_LIST[SHIFT]["Tips Split"] = tip_dist
    
def tip_calc():
    global EMP_NUM
    next_shift = True
    while next_shift:
        shifts(SHIFT)
        EMP_NUM = len(EMP_LIST[SHIFT]["Workers"])
        distips()
        next = input("Next shift?\nEnter 'Y' to continue").lower()
        if next != 'y':
            print(EMP_LIST)
            next_shift = False

tip_calc()
SHIFT += 1

