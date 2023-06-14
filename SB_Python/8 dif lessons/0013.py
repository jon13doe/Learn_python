def send_mail(from_name, ob):
    text = f"uv. vasys wtf {from_name}, {ob}"
    print(text)


# alt+ctr+l
send_mail('dunduk', 'kozel')


def get_sqrt(x):
    res = None if x < 0 else x ** 0.5


a = get_sqrt(49)
print(a)