import re
import sys
from datetime import datetime

def update_readme(problem_id, problem_name, problem_link, category="", learning=""):
    # Read current README
    with open('README.md', 'r') as file:
        content = file.read()
    
    # Update the solved count in badge
    solved_count = len(re.findall(r'✅ Solved', content)) + 1
    content = re.sub(r'img src="https://img\.shields\.io/badge/Solved-\d+-brightgreen"', 
                    f'img src="https://img.shields.io/badge/Solved-{solved_count}-brightgreen"', content)
    
    # Calculate days elapsed - assuming start date is March 10, 2025
    start_date = datetime(2025, 3, 10)
    today = datetime.now()
    days_elapsed = (today - start_date).days + 1  # +1 to include start day
    days_elapsed = max(days_elapsed, 0)  # Ensure non-negative
    
    # Calculate days remaining - assuming end date is April 30, 2025
    end_date = datetime(2025, 4, 30)
    days_remaining = (end_date - today).days + 1  # +1 to include end day
    days_remaining = max(days_remaining, 0)  # Ensure non-negative
    
    # Update progress tracker table
    remaining = 274 - solved_count
    content = re.sub(
        r'<td>(\d+)</td>\s+<td>(\d+)</td>\s+<td>(\d+)</td>\s+<td>(\d+)</td>\s+<td>(\d+)</td>', 
        f'<td>274</td>\n    <td>{solved_count}</td>\n    <td>{remaining}</td>\n    <td>{days_elapsed}</td>\n    <td>{days_remaining}</td>', 
        content
    )
    
    # Format learning content with toggle (even if empty)
    learning_content = "N/A" if not learning.strip() else learning
    learning_html = f"""
      <details>
        <summary>Show</summary>
        {learning_content}
      </details>
    """
    
    # Create the new problem row
    new_row = f'''  <tr>
    <td>{problem_id}</td>
    <td><a href="{problem_link}">{problem_name}</a></td>
    <td>✅ Solved</td>
    <td>{category}</td>
    <td>{learning_html}</td>
    <td><a href="solutions/{problem_id}.cpp">Solution</a></td>
  </tr>'''
    
    # Find where to append the new row (at the end of the table)
    table_end_pattern = r'</table>\s+## 📝 Milestones'
    match = re.search(table_end_pattern, content)
    if match:
        insert_position = match.start()
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