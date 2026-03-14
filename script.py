def is_balanced(config_string):
    config_string.split(" ")
    stack = []
    for index, character in enumerate(config_string):
        if config_string[index] == "[":
            stack.append("[")
        elif config_string[index] == "]":
            if stack:
                stack.pop()
            else:
                return False
    return True

sample = "[ [ ] ] ]"
print(is_balanced(sample))
