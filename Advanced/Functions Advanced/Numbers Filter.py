def even_odd_filter(**kwarks):
    if "odd" in kwarks:
        kwarks["odd"]=[n for n in kwarks["odd"] if n%2==1]
    if "even" in kwarks:
        kwarks["even"] = list(filter(lambda x: x % 2 ==0, kwarks["even"]))

    return dict(sorted(kwarks.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
