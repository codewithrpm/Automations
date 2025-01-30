import os

# Base directory to scan
base_path = r"D:\Automation\html_folder"

# Function to scan directory and build dictionary
def build_directory_structure(base_path):
    directory_structure = {}
    for root, dirs, files in os.walk(base_path):
        relative_root = os.path.relpath(root, base_path)
        if relative_root == ".":
            relative_root = "Root"
        directory_structure[relative_root] = files
    return directory_structure

# Function to generate the HTML file dynamically
def generate_html_from_structure(base_path, directory_structure):
    html_file_path = os.path.join(base_path, "index.html")
    with open(html_file_path, "w") as html_file:
        html_file.write("<html><body>\n")
        html_file.write("<h1>Dynamic Reports Directory</h1>\n")
        for folder, files in directory_structure.items():
            html_file.write(f"<h2>{folder}</h2>\n<ul>\n")
            for file in files:
                relative_path = os.path.join(folder, file).replace("\\", "/")
                html_file.write(f'<li><a href="{relative_path}" target="_blank">{file}</a></li>\n')
            html_file.write("</ul>\n")
        html_file.write("</body></html>")
    print(f"HTML file generated at: {html_file_path}")


def main():
    # Step 1: Build the dynamic directory structure
    directory_structure = build_directory_structure(base_path)

    # Step 2: Generate the HTML file
    generate_html_from_structure(base_path, directory_structure)

if __name__ == "__main__":
    main()
