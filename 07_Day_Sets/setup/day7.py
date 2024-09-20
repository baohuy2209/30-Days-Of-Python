st = set()
st = {"item1", "item2", "item3", "item4"}
fruits = {"banana", "orange", "mango", "lemon"}
print(len(st))
print(len(fruits))
print("Does set st container item3?", "item3" in st)

Fruits = {"banana", "orange", "mango", "lemon"}
print("mango" in fruits)

st.add("item5")
print(st)
st = {"item1", "item2", "item3", "item4"}
st.update(["item5", "item6", "item7"])
print(st)
