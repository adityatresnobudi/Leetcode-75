// Using strings.Fields (assigned to words variable) to get word only from string given
// if length of the words is 0 then return "" (s is an empty string)
// print words backward using two pointer (l and r) and strings.Join to join words

func reverseWords(s string) string {
    words := strings.Fields(s)
    if len(words) == 0 {
        return ""
    }

    l, r := 0, len(words)-1
    for l < r {
        words[l], words[r] = words[r], words[l]
        l++
        r--
    }
    return strings.Join(words, " ")
}