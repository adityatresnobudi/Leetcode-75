func isSubsequence(s string, t string) bool {
    i, j := 0, 0
    if len(s) == 0 {
        return true
    }
    if len(t) == 0 {
        return false
    }
    for j < len(t) {
        if s[i] == t[j] {
            i++
            j++
            if i == len(s) {
                return true
            }
            continue
        }
        j++
    }
    return false   
}
