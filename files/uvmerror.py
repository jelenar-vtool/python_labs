import argparse

def find_uvm_errors(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if "UVM_ERROR" in line:
                    print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to open file '{file_path}'.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find lines containing 'UVM_ERROR' in a text file.")
    parser.add_argument("file_path", help="Path to the text file")
    args = parser.parse_args()

    find_uvm_errors(args.file_path)