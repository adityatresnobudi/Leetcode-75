func compress(chars []byte) int {
    p_slice, p_result := 0, 0
    n := len(chars)

    for p_slice < n {
        i := p_slice + 1
        for i < n && chars[i] == chars[p_slice] {
            i++
        }

        chars[p_result] = chars[p_slice]
        p_result++
        if count := i - p_slice; count > 1 {
            num := []byte(strconv.FormatInt(int64(count), 10))
            for j := 0; j < len(num); j++ {
                chars[p_result+j] = num[j]
            }
            p_result += len(num)
        }
        p_slice = i
    }
    chars = chars[:p_result]
    return p_result
}
