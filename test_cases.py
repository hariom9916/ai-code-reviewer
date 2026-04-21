from reviewer import analyze_code

code = """
def find(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
"""

print(analyze_code(code))
