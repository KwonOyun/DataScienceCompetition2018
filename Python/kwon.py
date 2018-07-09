words = 'Connect Foundation'
if 'F'in words:
    words.lower()
    words = words[:7]+'&'+words[8:]
else:
    print(words)
print(words)