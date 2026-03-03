# LeetCode Visualization

A small FastAPI app that:
- takes a positive integer,
- generates a bit string using `change_num_to_bit`,
- builds a balanced binary tree from those bits,
- renders the tree with Graphviz,
- shows the image in the browser.

## Project Structure
- `app.py`: FastAPI server and visualization logic.
- `templates/index.html`: UI template rendered by FastAPI.
- `requirement.txt`: Python dependencies.
- `test.py`: quick Graphviz render sanity check.

## Prerequisites
1. Python 3.10+ (tested in this repo with Python 3.13 bytecode cache present).
2. Graphviz installed on your system.

On Windows, install Graphviz and ensure this path exists:
`C:\Program Files\Graphviz\bin`

`app.py` currently appends that exact Windows path to `PATH`.

## Setup
From the repository root:

```powershell
cd leetcode_visualization
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirement.txt
```

## Run the App
From `leetcode_visualization` directory:

```powershell
uvicorn app:app --reload
```

The app runs at:
- `http://127.0.0.1:8000`

Open that URL, enter a positive integer, and click **Generate Tree**.

## Optional: Graphviz Test
To confirm Graphviz rendering works:

```powershell
python test.py
```

If successful, it creates `test_tree.png` in the same folder.

## Notes
- Run from inside `leetcode_visualization` so `templates/` resolves correctly.
- Large input values may hit recursion limits (`RecursionError`).
