class Solution:

    # sender -> encode(list of strings -> string)
    # receiver -> decode(string->list of strings)
    # receiving end must be the same
    # strs[i] contains any possible characters out of 256 valid ASCII characters.

    # need to combine words into string but maintain order
    # ["Hello","World"] -> "HelloWorld" 
    # need something that shows when to split, can't be _ or similar since these are valid chars

    # Ascii numerical representation with _ seperates


    def encode(self, strs: List[str]) -> str:
        ascii_list = [list(map(ord, s)) for s in strs]
        return str(ascii_list)

    def decode(self, s: str) -> List[str]:
        print(s)

        s_list = eval(s) #convert from '[x,y,z]' (string) to [x,y,z] (list)"

        output = []
        for asc_word in s_list:
            #for each ascci char, convert to str and concat together via join to build back the word
            decode_word = "".join(chr(int(x)) for x in asc_word) 
            output+=[decode_word]
    
        return output
