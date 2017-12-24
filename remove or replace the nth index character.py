def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


def f(st,ch,po):
    li=list(st)
    li[po]=ch
    return ''.join(li)


print(mutate_string('abracadabra', 5, ''))
