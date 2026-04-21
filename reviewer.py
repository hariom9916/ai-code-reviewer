import re

def analyze_code(code):
    issues = []
    suggestions = []
    
    if "return" not in code:
        issues.append("Function may not return any value")
    
    if "for" in code and "return" in code and "else" not in code:
        issues.append("Possible missing return for edge cases")
        suggestions.append("Add default return like -1")
    
    if code.count("for") == 1:
        complexity = "O(n)"
    elif code.count("for") == 2:
        complexity = "O(n^2)"
    else:
        complexity = "Unknown"
    
    return issues, suggestions, complexity


def main():
    print("Paste code (type END to finish):")
    
    code = ""
    while True:
        line = input()
        if line.strip() == "END":
            break
        code += line + "\n"
    
    issues, suggestions, complexity = analyze_code(code)
    
    print("\nAnalysis:\n")
    
    for issue in issues:
        print("Issue:", issue)
    
    for suggestion in suggestions:
        print("Suggestion:", suggestion)
    
    print("Complexity:", complexity)


if __name__ == "__main__":
    main()
