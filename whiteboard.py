# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def solution(test):
    output = ''
    words = test.split(' ')
    store = ""
    for word in words:
        store = ""
        for char in word[-1::-1]:
            store += char
        output += f'{store} '
    return output.strip()

