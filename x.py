from anytree import Node, RenderTree

root = Node("Print")
gamma1 = Node("gamma", parent=root)
gamma2 = Node("gamma", parent=root)
gamma3 = Node("gamma", parent=gamma1)
substring = Node("substring", parent=gamma3)
length1 = Node("length", parent=substring)
s = Node("s", parent=substring)
gamma4 = Node("gamma", parent=substring)
n = Node("n", parent=gamma4)
length2 = Node("length", parent=gamma4)
s2 = Node("s", parent=length2)
str_node1 = Node("''", parent=length2)
str_node2 = Node("''", parent=length2)
eq1 = Node("eq", parent=substring)
s3 = Node("s", parent=eq1)
str_node3 = Node("''", parent=eq1)
int_node1 = Node("0", parent=eq1)
plus = Node("+", parent=eq1)
int_node2 = Node("1", parent=plus)
gamma5 = Node("gamma", parent=eq1)
gamma6 = Node("gamma", parent=gamma5)
conc = Node("Conc", parent=gamma6)
stem = Node("Stem", parent=conc)
s4 = Node("s", parent=stem)
gamma7 = Node("gamma", parent=gamma6)
substring2 = Node("substring", parent=gamma7)
stern = Node("Stern", parent=substring2)
s5 = Node("s", parent=substring2)
n2 = Node("-", parent=substring2)
m = Node("m", parent=substring2)
int_node3 = Node("1", parent=n2)
gamma8 = Node("gamma", parent=gamma7)
substring3 = Node("substring", parent=gamma8)
stern2 = Node("Stern", parent=substring3)
s6 = Node("s", parent=substring3)
n3 = Node("-", parent=substring3)
m2 = Node("m", parent=substring3)
int_node4 = Node("1", parent=n3)
m3 = Node("m", parent=gamma4)
rec = Node("rec", parent=gamma3)
function_form1 = Node("function_form", parent=rec)
length3 = Node("length", parent=function_form1)
s7 = Node("s", parent=function_form1)
eq2 = Node("eq", parent=length3)
s8 = Node("s", parent=eq2)
str_node4 = Node("''", parent=eq2)
int_node5 = Node("0", parent=eq2)
plus2 = Node("+", parent=eq2)
int_node6 = Node("1", parent=plus2)
gamma9 = Node("gamma", parent=eq2)
length4 = Node("length", parent=gamma9)
stern3 = Node("Stern", parent=length4)
s9 = Node("s", parent=length4)

ast_tree = RenderTree(root)
for pre, _, node in ast_tree:
    print(f"{pre}{node.name}")
