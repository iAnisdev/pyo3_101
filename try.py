import pyo3_101 as p1

sum = p1.sum_as_string(1,2)
print(f"{sum} as type {type(sum)}")

john = p1.say_hello("John" , "Pycon")
print(john)

# test check_reg
print(p1.check_reg("reg_list.txt", "john"))
print(p1.check_reg("reg_list.txt", "jane"))
print(p1.check_reg("reg_list.txt", "adam"))
print(p1.check_reg("reg_list.txt", "mary"))

# test check_reg with a non-existent file
# print(p1.check_reg("reg_list2.txt", "john"))

# test count_att
budget_dict = {
"John": 850,
"Susan": 790,
"Peter":1030,
"Judy": 540,
}
print(p1.travel_avg(budget_dict))

# test Attendee
print(f"Number of attendees are {p1.Attendee.cur_reg_num}")

me = p1.Attendee('Cheuk', True)
print(me.name, me.speaker, me.reg_num)
print(f"Number of attendees are {p1.Attendee.cur_reg_num}")

keynote = p1.Attendee('John', True)
print(keynote.name, keynote.speaker, keynote.reg_num)
keynote.name = 'Jon'
print(keynote.name, keynote.speaker, keynote.reg_num)

print(f"Number of attendees are {p1.Attendee.cur_reg_num}")
