func mergeAlternately(word1 string, word2 string) string {
    res := ""
    if len(word1) >= len(word2) {
        for i := 0; i < len(word2); i++ {
            res += string(word1[i])
            res += string(word2[i])
        }
        res += word1[len(word2):len(word1)]
        return res
    }
    for i := 0; i < len(word1); i++ {
        res += string(word1[i])
        res += string(word2[i])
    }
    res += word2[len(word1):len(word2)]
    return res
}