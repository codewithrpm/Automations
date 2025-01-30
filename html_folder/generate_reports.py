import os


base_path = r"D:\Automation\html_folder"

# Hardcoded folder and file structure
phases = {
    "Phase1": ["checklist1.pdf", "report_image.jpg", "data.xlsx", "presentation.pptx", "note.txt", "summary.csv"],
    "Phase2": ["checklist1.html", "checklist2.html", "checklist3.html"],
    "Phase3": ["checklist1.html"]
}

# Create the folder structure and files
def create_folders_and_files(base_path, phases):
    for phase, reports in phases.items():
        phase_path = os.path.join(base_path, phase)
        os.makedirs(phase_path, exist_ok=True)  # Create phase folder
        for report in reports:
            report_path = os.path.join(phase_path, report)
            with open(report_path, "w") as f:
                f.write(f"<h1>{report} for {phase}</h1>")  # Sample content

# Generate HTML file with links to all files
def generate_html(base_path, phases):
    html_file_path = os.path.join(base_path, "index.html")
    with open(html_file_path, "w") as html_file:
        html_file.write("<html><body>\n")
        html_file.write("<h1>Reports Directory</h1>\n")
        for phase, reports in phases.items():
            html_file.write(f"<h2>{phase}</h2>\n<ul>\n")
            for report in reports:
                relative_path = os.path.join(phase, report)
                html_file.write(f'<li><a href="{relative_path}" target="_blank">{report}</a></li>\n')
            html_file.write("</ul>\n")
        html_file.write("</body></html>")
    print(f"HTML file generated at: {html_file_path}")

# Main function
def main():
    create_folders_and_files(base_path, phases)
    generate_html(base_path, phases)

if __name__ == "__main__":
    main()
