import os
import sys

def dumpdb():
    # i know dumping usuall means exporting but were literally deleting all .db files in the root folder of your project
    print("WARNING: This will delete all .db files in the project root folder!")
    confirmation = input("Type 'DELETE' to confirm: ")
    if confirmation == 'DELETE':
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for filename in os.listdir(project_root):
            if filename.endswith('.db'):
                file_path = os.path.join(project_root, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
        print("All .db files have been deleted.")
    else:
        print("Operation cancelled.")
        sys.exit()
    