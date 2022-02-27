def hackerrankInString(s):
    # Write your code here
    word = 'hackerrank'
    l = len(word)
    i = 0
    for char in s:
        if char == word[i]:
            i += 1
            if i == l:
                return "YES"
    
    return "NO"
