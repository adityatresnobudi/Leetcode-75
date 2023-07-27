func mergeAlternately(word1 string, word2 string) string {
    var newWord = ""
    if len(word1) > len(word2) {
        for i := 0; i < len(word2); i++ {
            newWord = newWord + word1[i:i+1] + word2[i:i+1]
        }
        newWord = newWord + word1[len(word2):len(word1)]
    } else if len(word1) < len(word2) {
        for i := 0; i < len(word1); i++ {
            newWord = newWord + word1[i:i+1] + word2[i:i+1]
        }
        newWord = newWord + word2[len(word1):len(word2)]
    } else {
        for i := 0; i < len(word1); i++ {
            newWord = newWord + word1[i:i+1] + word2[i:i+1]
        }
    }
    return newWord
}
