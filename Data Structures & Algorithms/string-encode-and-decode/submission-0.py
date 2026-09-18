class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for s in strs:
            encoded_str.append(str(len(s)) + "#" + s)
        return ''.join(encoded_str)


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            delimiter_index = s.find("#", i)
            length = int(s[i:delimiter_index])
            start = delimiter_index + 1
            end = start + length
            decoded_str = s[start:end]

            decoded_strs.append(decoded_str)
            i = end
        return decoded_strs

            
            