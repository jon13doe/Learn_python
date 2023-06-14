f = print
a = {1, 23, 456}
f(a)
print = 'eto bila funkcia print'
f(print)
print = f


def send_mail(from_name, ob):
    text = f"uv. vasys wtf {from_name}, {ob}"
    print(text)


# alt+ctr+l
send_mail('dunduk', 'kozel')
