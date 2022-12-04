country = input().split(", ")
capitals = input().split(", ")

#final_result={country[index]:capitals[index] for index in range(len(country))}
final_result = dict(zip(country, capitals))
for (key, value) in final_result.items():
    print(f"{key} -> {value}")
