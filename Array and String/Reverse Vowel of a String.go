// make isVowel function to check is the character is Vowel or not
// isVowel will accept rune as input (accessing array in specific location will access byte or rune)
// isVowel will make boolean output (if vowel True viceversa)
// reversalVowels will iterate string s using two pointer l and r
// pointer will look for the first vowel it encounter and swap it with each other

func isVowel (character rune) bool {
    switch character {
        case 'a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O':
        return true
        default:
        return false
    }
}
func reverseVowels(s string) string {
    newS := []rune(s)
    n := len(newS)
    l, r := 0, n-1
    for l < r {
        for l < r && !isVowel(newS[l]) {
            l++
        }
        for r > l && !isVowel(newS[r]) {
            r--
        }
        newS[l], newS[r] = newS[r], newS[l]
        l++
        r--
    }
    return string(newS)
}
