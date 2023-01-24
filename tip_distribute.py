from art import logo

todo = "TODO LIST: Need to assign and save tip_dist to emp_list.\nProbably need to learn dictionaries to do that....\n\n\n"

stay_open = True
shift_total = 1
emp_list = []
tip_total = 0


print(logo)
print("This is a 'very' simple tip distribution calculator.\nTips are first distributed into shifts.\nThen evenly across number of employees who worked that shift.\n\n")
print(todo)

while stay_open:
    if shift_total > 1:
        tip_total = float(input(f"Tip total for shift {shift_total}:\n$ ")) - tip_total
    elif shift_total <= 1:
        tip_total += float(input(f"Tip total of shift {shift_total}:\n$ "))
    emp_num = int(input("How many people worked?\n"))
    tip_dist = round(tip_total / emp_num, 2)



    #Gets list of employee names
    for i in range(1, emp_num + 1):
        name_add = input(f"Name of employee number {i}: ")
        if name_add not in emp_list:
            emp_list += [name_add]

    #prints out employees tip total
    print(f"Shift {shift_total} made ${tip_total}")
    for emp in emp_list:
        print(f"{emp} made ${tip_dist}")

    #Continue?
    stop_p = input("Press enter to continue to next shift. Or 'q' to quit.\n").lower()
    if stop_p == "q":
        stay_open = False
    shift_total += 1