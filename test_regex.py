import re

pattern = r"^/((?!assets/|.*\..*).*)$"
test_cases = [
    ("/", True),
    ("/diagnose", True),
    ("/explorer", True),
    ("/dashboard", True),
    ("/assets/index-C4NPAlh5.js", False),
    ("/assets/index-cwdZKs0d.css", False),
    ("/favicon.ico", False),
    ("/logo.svg", False)
]
for path, expected in test_cases:
    matched = bool(re.match(pattern, path))
    status = "PASS" if matched == expected else "FAIL"
    print(f"{path:30} Matched: {matched} | Expected: {expected} | {status}")
