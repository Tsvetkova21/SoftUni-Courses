def sorting_cheeses(**cheeses_dict):
    cheeses_dict = sorted(
            cheeses_dict.items(),
            key=lambda x: (-len(x[1]), x[0]))
    result = []
    for (cheese_name, quantities) in cheeses_dict:
        result.append(cheese_name)
        result.extend(sorted(quantities,reverse=True))
    return "\n".join([str(x) for x in result])

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
