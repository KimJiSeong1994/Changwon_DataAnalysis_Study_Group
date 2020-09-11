# ================================================== [ setting ] ==================================================
import re

word = "grail"
sent = "a scratch"

# print(word[0:3])
# print(sent[2:-1])
# print(sent[2:len(sent)])
# print(sent[2 :])
# print(sent[ ::2])

# print("black Knight".capitalize())
# print("It's just a flesh wound!".count("u"))
# print("Halt!. Who goes there?".startswith("Halt"))
# print("coconut".endswith("nut"))
# print("It's just a flesh wound!".find("u"))
# print("It's ust a flesh wound!".index("scratch"))
# print("old woman".isalpha())
# print("37".isdecimal())
# print("I'm 37".isalnum())
# print("Black Knight".lower())
# print("Black Knight".upper())
# print("flesh wound!".replace("flesh wound", "scratch"))
# print("I'm not dead".strip())
# print("NI! NI! NI! NI!".split(sep = " "))
# print("3,4".partition(sep = ","))
# print("nine".center(10))
# print("9".zfill(5))

d1 = '40°'
m1 = "46'"
s1 = '52.837"'
u1 = 'N'
d2 = '73°'
m2 = "58'"
s2 = '26.302"'
u2 = 'W'
coords = ' '.join([d1, m1, s1, u1, d2, m2, s2, u2])
# print(coords)

multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together. 
"""
# print(multi_str)

multi_str_split = multi_str.splitlines()
# print(multi_str_split)

guard = multi_str_split[::2]
# print(guard)

guard = multi_str.replace("Guard: ", "").splitlines()[::2]
# print(guard)

var = 'flesh wound'
s = "It's just a {}!"
# print(s.format(var))
# print(s.format('scratch'))

s = """Black Knight: 'Tis but a {0}.
King Arthur: A {0}? Your arm's off!
"""
# print(s.format('scratch'))

s = 'Hayden Planetarium Coordinates: {lat}, {lon}'
# print(s.format(lat='40.7815° N', lon='73.9733° W'))

# print('Some digits of pi: {}'.format(3.14159265359))
# print("In 2005, Lu Chao of China recited {:,} digits of pi".format(67890))
# print("I remember {0:.4} or {0:.4%} of what Lu Chao recited".format(7/67890))
# print("My ID number is {0:05d}".format(42))

s = 'I only know %d digits of pi' % 7
# print(s)
# print('Some digits of %(cont)s: %(value).2f' % {'cont': 'e', 'value': 2.718})


var = 'flesh wound'
s = f"It's just a {var}!"
# print(s)

lat='40.7815°N'
lon='73.9733°W'
s = f'Hayden Planetarium Coordinates: {lat}, {lon}'
# print(s)

tele_num = '1234567890'
m = re.match(pattern='\d\d\d\d\d\d\d\d\d\d', string=tele_num)
print(bool(m))

tele_num_spaces = '123 456 7890'
m = re.match(pattern='\d{10}', string=tele_num_spaces)
# print(m)


p = '\d{3}\s?\d{3}\s?\d{4}'
m = re.match(pattern=p, string=tele_num_spaces)
# print(m)


tele_num_space_paren_dash = '(123) 456-7890'
p = '\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=tele_num_space_paren_dash)
# print(m)
cnty_tele_num_space_paren_dash = '+1 (123) 456-7890'
p = '\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
# print(m)

p = re.compile('\d{10}')
s = '1234567890'
m = p.match(s)
# print(m)