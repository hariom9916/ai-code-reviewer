# 🤖 AI Code Reviewer

An intelligent code analysis tool that evaluates code for correctness, efficiency, and potential bugs. Designed to simulate real-world software engineering review processes.

---

## 🚀 Features

* Detects common logical errors and bugs
* Provides time complexity estimation
* Suggests improvements for cleaner code
* Identifies edge cases

---

## 📌 Example

### Input

```python
def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
```

### Output

* Issue: Missing return if element not found
* Suggestion: Add `return -1`
* Time Complexity: O(n)

---

## 🧰 Tech Stack

Python, Rule-based analysis

---

## ▶️ Run

```bash
python reviewer.py
```
