test = r"""
-..-
. \.
/\ \
 /\/
/`' 
`--'
"""

top_left = """ .--..-
/ .. \.
\ \/\ \\
 \/ /\/
 / /\/ 
/ /\ \/
"""

top_right = r"""-..--.
. \.. \
/\ \/ /
 /\/ /
/\/ /\
\ \/\ \
"""
#To Pus
components = top_left.splitlines()
# print(components)

print(top_left, end="")
print(top_right, end="")

Knot_components = [r"-..-",
                   r". \.",
                   r"/\ "'\\',
                   r" /\/",
                   r"/`' ",
                   r"`--'"]

# for component in Knot_components:
#     for i in range(10):
#         print(component, end="")
#     print()