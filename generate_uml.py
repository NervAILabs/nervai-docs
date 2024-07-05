import os
import subprocess

# Check if docs/uml directory exists
uml_dir = "images/uml"
os.makedirs(uml_dir, exist_ok=True)

# Check if pyreverse is installed
try:
    subprocess.run(["pyreverse", "--help"], stdout=subprocess.PIPE)
except FileNotFoundError:
    print("pyreverse is not installed. Please install it using `pip install pylint`")
    exit(1)

# Define modules to generate UML diagrams for
modules = {
    "vml_sdk": "vml-sdk/vml_sdk/",
    "vml_server": "vml-server/vml_server/",
    "metinor_profiler": "metinor/metinor/profiler/",
    "metinor_pruning": "metinor/metinor/optimization/pruning/",
    "metinor_quantization": "metinor/metinor/optimization/quantization/",
    "metinor_visualization": "metinor/metinor/visualization/architecture/",
}

# Generate UML diagrams
ext = "png"
for project, path in modules.items():
    subprocess.run(
        [
            "pyreverse",
            "-o",
            ext,
            "-d",
            uml_dir,
            # NOTE: Remove the following flag to include methods and attributes in the UML diagram
            #       This is disabled to reduce the clutter in the diagram
            "-k",    # Show only class names (no methods or attributes)
            "-mn",   # Do not show qualified module names
            "--colorized",  # Colorize the diagram
            "--ignore=tests",
            "--project=" + project,
            f"../{path}",
        ]
    )

# Delete all packages_*.[ext] files
for file in os.listdir(uml_dir):
    if file.startswith("packages_") and file.endswith(ext):
        os.remove(os.path.join(uml_dir, file))