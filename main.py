def even_numbers(n):
    sane=[]

    for i in n:
        if (i%2==0):
            sane.append(i)
    return sane


def odd_numbers(n):
    sane=[]

    for i in n:
        if (i%2!=0):
            sane.append(i)
    return sane

        