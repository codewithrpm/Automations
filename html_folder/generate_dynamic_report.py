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

# Function to generate the HTML file with a grey theme
def generate_html_from_structure(base_path, directory_structure):
    html_file_path = os.path.join(base_path, "index.html")
    with open(html_file_path, "w") as html_file:
        html_file.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Reports Directory</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5; /* Light grey background */
            color: #333;
        }
        header {
            background-color: #4a4a4a; /* Dark grey header */
            color: white;
            padding: 20px;
            text-align: center;
        }
        header h1 {
            margin: 0;
            font-size: 28px;
        }
        main {
            padding: 30px;
            max-width: 1200px;
            margin: 0 auto;
            background: #ffffff; /* White background for content */
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #4a4a4a; /* Dark grey for headings */
            font-size: 20px;
            margin-top: 30px;
            border-bottom: 2px solid #d1d1d1; /* Light grey border */
            padding-bottom: 5px;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
            font-size: 16px;
        }
        a {
            text-decoration: none;
            color: #007acc; /* Blue links for contrast */
            font-weight: 500;
            transition: color 0.3s ease-in-out;
        }
        a:hover {
            color: #005b99; /* Darker blue on hover */
        }
        .folder-section {
            margin-bottom: 20px;
        }
        .toc {
            margin-bottom: 30px;
            padding: 15px;
            background: #e0e0e0; /* Light grey for TOC background */
            border: 1px solid #bfbfbf; /* Medium grey border */
            border-radius: 5px;
        }
        .toc h2 {
            font-size: 18px;
            margin: 0 0 10px 0;
            color: #4a4a4a; /* Dark grey for TOC heading */
        }
        .toc ul {
            list-style-type: none;
            padding-left: 15px;
        }
        .toc li {
            margin: 5px 0;
        }
        footer {
            margin-top: 30px;
            text-align: center;
            font-size: 14px;
            color: #888;
            padding: 10px 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Dynamic Reports Directory</h1>
    </header>
    <main>
        <div class="toc">
            <h2>Table of Contents</h2>
            <ul>
""")
        # Add a Table of Contents
        for folder in directory_structure.keys():
            html_file.write(f'<li><a href="#{folder}">{folder}</a></li>\n')

        html_file.write("""
            </ul>
        </div>
""")
        # Add folders and files with links
        for folder, files in directory_structure.items():
            html_file.write(f'<div class="folder-section" id="{folder}">\n')
            html_file.write(f'<h2>{folder}</h2>\n<ul>\n')
            for file in files:
                relative_path = os.path.join(folder, file).replace("\\", "/")
                html_file.write(f'<li><a href="{relative_path}" target="_blank">{file}</a></li>\n')
            html_file.write("</ul>\n</div>\n")

        # Add footer
        html_file.write("""
    </main>
    <footer>
        Dynamic Reports Directory &copy; 2025
    </footer>
</body>
</html>
""")
    print(f"Professional HTML report with grey theme generated at: {html_file_path}")

# Main function
def main():
    # Step 1: Build the directory structure
    directory_structure = build_directory_structure(base_path)

    # Step 2: Generate the professional HTML report
    generate_html_from_structure(base_path, directory_structure)

if __name__ == "__main__":
    main()
