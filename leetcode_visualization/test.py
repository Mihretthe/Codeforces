import os
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

from graphviz import Digraph

dot = Digraph()
dot.node("root", "Testoot")
dot.node("left", "Left")
dot.node("right", "Right")

# Fixed: use .edge() calls instead of .edges() with short strings
dot.edge("root", "left")
dot.edge("root", "right")

try:
    dot.render("test_tree", format="png", cleanup=True, quiet=False)
    print("Success! Check for test_tree.png")
except Exception as e:
    print("Failed:", str(e))