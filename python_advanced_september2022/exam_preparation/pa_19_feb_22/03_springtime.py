def start_spring(**kwargs):
    collection_dict = {}
    result = []

    for name, type in kwargs.items():
        if type not in collection_dict:
            collection_dict[type] = []
        collection_dict[type].append(name)

    sorted_spring_collection = sorted(collection_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for el in sorted_spring_collection:
        result.append(f"{el[0]}:")
        for obj in sorted(el[1]):
            result.append(f"-{obj}")

    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))