func compress(chars []byte) int {
    count, index := 1, 0
    for i := 1; i <= len(chars); i++ {
        if i < len(chars) && chars[i] == chars[i - 1] {
            count++
            continue
        }

        chars[index] = chars[i - 1]
        index++
        if count > 1 {
            for _, num := range strconv.Itoa(count) {
                chars[index] = byte(num)
                index++
            }
        }
        count = 1
    }

    return index
}