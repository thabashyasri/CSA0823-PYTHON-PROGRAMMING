def add_item_buggy(item, order=[]):
    order.append(item); return order
 
def add_item(item, order=None):
    if order is None:
        order = []                      # TODO 1: fresh list on every call
    order.append(item); return order
 
print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print(add_item("Tea"), add_item("Vada"))
print("add_item_buggy.__defaults__ =", add_item_buggy.__defaults__)
print("add_item.__defaults__       =", add_item.__defaults__)
 
# Parameters: positional, keyword, default; multiple return values
GST_RATE = 0.05
def bill(items, prices, gst_rate=GST_RATE):
    total = sum(prices[i] for i in items)
    gst = round(total * gst_rate, 2)
    return total, gst, round(total + gst, 2)       # tuple of 3 values
prices = {"Tea": 10, "Vada": 15, "Meals": 60}
t, g, grand = bill(["Tea", "Vada"], prices)
print("positional :", t, g, grand)
print("keyword    :", bill(prices=prices, items=["Meals"], gst_rate=0.12))
 
# Three independent customers
print("\nThree customers:")
orders = []
for menu in (["Tea", "Vada"], ["Meals"], ["Tea", "Tea", "Meals"]):
    o = None
    for it in menu: o = add_item(it, o)
    orders.append(o)
print(orders, "| all different objects:", len({id(o) for o in orders}) == 3)
 
# local / global / nonlocal
x = "global"
def local_demo():
    x = "local"; return x
def global_demo():
    global x; x = "changed by global_demo"
def outer():
    count = 0
    def inner():
        nonlocal count; count += 1; return count
    inner(); inner(); return count
print("\nlocal_demo() ->", local_demo(), "| x still:", x)
global_demo(); print("after global_demo(), x =", x)
print("outer() with nonlocal ->", outer())
try:
    def bad(): 
        y += 1
    y = 0; bad()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
 
# Alternative: closure keeps the order
def make_order():
    order = []
    def add(item): order.append(item); return list(order)
    return add
a, b = make_order(), make_order()
a("Tea"); a("Vada"); print("closure customer A:", a("Meals"), "| customer B:", b("Tea"))
