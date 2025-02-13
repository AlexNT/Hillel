def between_markers(text: str, begin: str, end: str) -> str:
    fr = text.find(begin)
    se = text.find(end)
    if fr == -1 and se == -1:
        return text
    elif fr == -1 and se > -1:
        return text[:se]
    elif fr > -1 and se == -1:
        return text[fr + len(begin):]
    return text[fr+len(begin):se]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")