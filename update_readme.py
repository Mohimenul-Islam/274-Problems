import re
import sys

def update_readme(problem_id, problem_name, problem_link, category="", learning=""):
    # Read current README
    with open('README.md', 'r') as file:
        content = file.read()
    
    # Update the solved count in badge
    solved_count = len(re.findall(r'✅ Solved', content)) + 1
    content = re.sub(r'img src="https://img\.shields\.io/badge/Solved-\d+-brightgreen"', 
                    f'img src="https://img.shields.io/badge/Solved-{solved_count}-brightgreen"', content)
    
    # Update progress tracker table
    remaining = 274 - solved_count
    content = re.sub(r'<td>\d+</td>\s+<td>\d+</td>', 
                    f'<td>{solved_count}</td>\n    <td>{remaining}</td>', content)
    
    # Add the new problem to the table
    new_row = f'''  <tr>
    <td>{problem_id}</td>
    <td><a href="{problem_link}">{problem_name}</a></td>
    <td>✅ Solved</td>
    <td>{category}</td>
    <td>{learning}</td>
    <td><a href="solutions/{problem_id}.cpp">Solution</a></td>
  </tr>'''
    
    # Find where to insert the new row
    table_pattern = r'<table>\s+<tr>\s+<th>ID</th>.*?</tr>\s+'
    match = re.search(table_pattern, content, re.DOTALL)
    if match:
        insert_position = match.end()
        content = content[:insert_position] + new_row + '\n' + content[insert_position:]
    
    # Write updated README
    with open('README.md', 'w') as file:
        file.write(content)
    
    print(f"Added problem {problem_id}: {problem_name} to README.md")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python update_readme.py <problem_id> <problem_name> <problem_link> [category] [learning]")
        sys.exit(1)
    
    problem_id = sys.argv[1]
    problem_name = sys.argv[2]
    problem_link = sys.argv[3]
    category = sys.argv[4] if len(sys.argv) > 4 else ""
    learning = sys.argv[5] if len(sys.argv) > 5 else ""
    
    update_readme(problem_id, problem_name, problem_link, category, learning)

#python3 update_readme.py "B" "B" "https://vjudge.net/contest/696883#problem/B" "Bitmask / Complete Search" "N/A"