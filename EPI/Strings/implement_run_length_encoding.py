# Run-length Econding (RLE) compression offers a fast way to do efficient on-the-fly compression and decompression of strings. The idea is simple--encode successive repeated characters by the repetition count and the character. For example, the RLE of "aaaabcccaa" is "4a1b3c2a".

# Implement run-length encoding and decoding functions.Assume the string to be encoded consists of letters of the alphabet.

class RLE:
    def compress(self, data):
        if not data: return ""

        prev = None
        count = 0
        ind = 0
        res = ""

        while ind < len(data):
            if data[ind] == prev:
                count += 1
            else:
                if prev:
                    res += "%s%s" % (count + 1, prev)

                count = 0
                prev = data[ind]
            ind += 1

        res += "%s%s" % (count, prev)
        return res

    def decompress(self, data):
        if not data: return ""

        res = ""
        for i in range(0, len(data), 2):
            res += int(data[i]) * data[i + 1]

        return res