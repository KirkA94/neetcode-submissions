class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded_words = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            word_length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + word_length

            decoded_words.append(s[word_start:word_end])
            i = word_end

        return decoded_words