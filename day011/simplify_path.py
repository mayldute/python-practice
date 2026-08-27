"""
Task:
Simplify an absolute Unix-style file path.

Requirements:
- Accept an absolute Unix-style path as a string.
- The path starts with `/`.
- `/` separates directories.
- `.` represents the current directory.
- `..` represents the parent directory.
- Multiple consecutive `/` characters should be treated as one.
- The result must start with `/`.
- The result must not end with `/`, unless the result is the root `/`.
- `..` cannot move above the root directory.
- Return the simplified path.

Examples:
    "/home/" → "/home"
    "/home//user/" → "/home/user"
    "/home/./user" → "/home/user"
    "/home/user/../documents" → "/home/documents"
    "/../" → "/"
    "/a/../../b" → "/b"
    "/a/./b/../../c/" → "/c"
    "/" → "/"
"""


def simplify_path(path: str) -> str:
    parts = path.split("/")
    stack = []

    for part in parts:
        if not part or part == ".":
            continue

        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    print(stack)

    return "/" + "/".join(stack)
