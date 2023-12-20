func isVowel(c rune) bool {
    vowel := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for _, v := range vowel {
        if c == v {
            return true
        }
    }
    return false
}

func reverseVowels(s string) string {
    l, r := 0, len(s)-1
    runes := make([]rune, len(s))
    for idx, r := range s {
        runes[idx] = r
    }

    for l < r {
        if !isVowel(runes[r]) {
            r--
            continue
        }

        if !isVowel(runes[l]) {
            l++
            continue
        }

        runes[l], runes[r] = runes[r], runes[l]
        l++
        r--
    }

    return string(runes)
}