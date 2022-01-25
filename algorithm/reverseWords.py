
def reverseWords(s: str) -> str:
    if not s: return ""
    new_s = []
    s_list = s.split(" ")
    for word in s_list:
        new_s.append(word[::-1])
    return " ".join(new_s)

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(f'Before: {s}')
    new_s = reverseWords(s)
    print(f'After: {new_s}')
    