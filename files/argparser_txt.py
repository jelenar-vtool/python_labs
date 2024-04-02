import argparse
import os

def parse_doc_reg(file_path):
    defines_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line matches the expected pattern
            if "(" in line and ")" in line and ":" in line:
                addr_part, define_part = line.split(")?")
                addr = addr_part.strip().split("==")[1].strip()
                define = define_part.strip().split(":")[0].strip()
                # Append formatted line to list
                defines_lines.append(f"`define {define} 32'h{addr}\n")
    
    return defines_lines

def write_defines_file(defines_lines, output_dir):
    output_file = os.path.join(output_dir, "defines.txt")
    with open(output_file, 'w') as file:
        file.writelines(defines_lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse doc_reg.txt and create defines.txt")
    parser.add_argument("file_path", help="Path to the input file (doc_reg.txt)")
    parser.add_argument("-o", "--output-dir", help="Output directory for defines.txt (default: current directory)", default=os.getcwd())
    args = parser.parse_args()

    # Parse doc_reg.txt and get defines lines
    defines_lines = parse_doc_reg(args.file_path)

    if defines_lines:
        # Write the defines lines to defines.txt
        write_defines_file(defines_lines, args.output_dir)
        print(f"File 'defines.txt' has been created successfully in '{args.output_dir}'.")
    else:
        print("No valid lines found in doc_reg.txt.")
#defines sacuvano u users(Jelena Rajkovic)
