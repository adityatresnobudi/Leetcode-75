func gcd(num1, num2 int) int {
    for num2 != 0 {
        num1, num2 = num2, num1%num2
    }

    return num1
}
func gcdOfStrings(s1 string, s2 string) string {
    if s1+s2 != s2+s1 {
        return ""
    }

    length := gcd(len(s1), len(s2))
    return s1[:length]
}