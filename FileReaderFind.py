import re

def search_and_replace(file_path, search_query, replace_query=None, marker_symbol=None):
    line_numbers = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_query in line:
                line_numbers.append(i+1)
                if replace_query is not None:
                    if marker_symbol is not None:
                        lines[i] = re.sub(search_query, f"{marker_symbol}{replace_query}{marker_symbol}", lines[i])
                    else:
                        lines[i] = lines[i].replace(search_query, replace_query)
    
    with open(file_path, 'w') as f:
        f.writelines(lines)
        
    return line_numbers

if __name__ == "__main__":
    file_path = input("Enter file path: ")
    search_query = input("Enter search query: ")
    replace_query = input("Enter replace query: ")
    marker_symbol = input("Enter marker symbol: ")
    line_numbers = search_and_replace(file_path, search_query, replace_query, marker_symbol)
    print(line_numbers)