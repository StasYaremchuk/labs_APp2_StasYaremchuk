def boyer_moore_search(haystack, needle):
    def str_length(s):
        count = 0
        for _ in s:
            count += 1
        return count

    def build_bad_char_table(pat):
        table = {}
        m = str_length(pat)
        i = 0
        while i < m - 1:
            table[pat[i]] = m - i - 1
            i += 1
        return table

    n = str_length(haystack)
    m = str_length(needle)
    if m == 0 or m > n:
        return []

    bad_char_table = build_bad_char_table(needle)
    result = []
    i = 0

    while i <= n - m:
        j = m - 1
        while j >= 0 and needle[j] == haystack[i + j]:
            j -= 1
        if j < 0:
            result.append(i)
            i += m
        else:
            shift = bad_char_table.get(haystack[i + j], m)
            i += shift

    return result
