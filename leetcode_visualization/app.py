import os
import base64
import tempfile
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Force Graphviz PATH (adjust if your install path is different)
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

from graphviz import Digraph

app = FastAPI(title="Balanced Binary Tree Visualizer")

# Tell FastAPI where your templates folder is
templates = Jinja2Templates(directory="templates")

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def change_num_to_bit(num):
    if num == 1:
        return "0"

    before = change_num_to_bit(num - 1)
    
    # invert
    after = []
    for i in before:
        if i == "1":
            after.append("0")
        else:
            after.append("1")
    
    # reverse
    after = after[::-1]

    return before + "1" + "".join(after)

def build_tree(bits):
    if not bits:
        return None
    mid = len(bits) // 2
    root = TreeNode(bits[mid])
    root.left = build_tree(bits[:mid])
    root.right = build_tree(bits[mid + 1:])
    return root

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "image_base64": None,
            "input_number": None,
            "generated_bits": None,
            "error": None
        }
    )

@app.post("/visualize", response_class=HTMLResponse)
async def visualize(
    request: Request,
    number: int = Form(...)
):
    input_number = number
    error = None
    generated_bits = None
    image_base64 = None

    if number < 1:
        error = "Please enter a positive integer ≥ 1"
    else:
        try:
            # Generate bits using your function
            generated_bits = change_num_to_bit(number)
            
            # Convert to list of integers for the tree
            bit_list = [int(c) for c in generated_bits]

            root = build_tree(bit_list)
            if not root:
                error = "Could not build tree from generated bits"

            if not error:
                # Build graphviz
                dot = Digraph(format='png')
                dot.attr(rankdir='TB')
                dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')

                def add_node(node):
                    if node is None:
                        return
                    nid = str(id(node))
                    dot.node(nid, str(node.val))
                    if node.left:
                        dot.edge(nid, str(id(node.left)))
                        add_node(node.left)
                    if node.right:
                        dot.edge(nid, str(id(node.right)))
                        add_node(node.right)

                add_node(root)

                # Render to temp file
                with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
                    png_path = tmp.name

                base_name = png_path[:-4]
                dot.render(base_name, format='png', cleanup=True, quiet=False)

                if os.path.exists(png_path):
                    with open(png_path, "rb") as f:
                        image_base64 = base64.b64encode(f.read()).decode("utf-8")
                    
                    # Clean up
                    try:
                        os.unlink(png_path)
                    except:
                        pass
                else:
                    error = "Failed to generate image file"

        except RecursionError:
            error = "Number is too large — recursion depth exceeded"
        except Exception as e:
            error = f"Error: {str(e)}"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "image_base64": image_base64,
            "input_number": input_number,
            "generated_bits": generated_bits,
            "error": error
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)