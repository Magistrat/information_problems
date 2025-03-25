def is_balanced(s: str) -> bool:
    stack = []
    brackets = {')': '(', ']': '[', '}': '{', '>': '<'}

    for char in s:
        if char in brackets.values():  # Если открывающая скобка
            stack.append(char)
        elif char in brackets:  # Если закрывающая скобка
            if not stack or stack.pop() != brackets[char]:
                return False
    return not stack  # Стек должен быть пустым в конце


if __name__ == '__main__':
    print(is_balanced("()"))  # True
    print(is_balanced("({[<>]})"))  # True
    print(is_balanced("({[< >]})"))  # True (пробелы игнорируются)
    print(is_balanced("({[<)]}"))  # False
    print(is_balanced("("))  # False (незакрытая скобка)
    print(is_balanced(")("))  # False (неправильный порядок)
