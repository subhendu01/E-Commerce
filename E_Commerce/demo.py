# family = {"umakant" : "Subhendu", "Ramanath": "Guddy", "Purna": "Barsha", "Rajani": "Tejas"}
# for parent, son in family.items():
#     print(f"{parent} is {son}'s dad")
#
# Prizes = ['Gold','Silver','Bronze','Nothing','Zilch']
# for place, prize in enumerate(Prizes):
#     print(f"Place number {place+1} gets {prize}")
#
Families = {'Peter':['Paul','Patty'], 'Jim':['Tommy','Timmy','Tammy'], 'Carlos':['Diego']}
for Parent, Children in Families.items():
    # print(Parent, Children)
    # print(f"{Parent} has {len(Children)} kid(s):" )
    print(f"{', and '.join([Child for Child in Children])}")