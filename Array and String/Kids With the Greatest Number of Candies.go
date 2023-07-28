func maxCandies(candies []int) int {
    var value int
    for i := 0; i < len(candies); i++ {
        if value < candies[i] {
            value = candies[i]
        }
    }
    return value
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
    var condition []bool
    for i := 0; i < len(candies); i++ {
        if candies[i] + extraCandies >= maxCandies(candies) {
            condition = append(condition, true)
        } else {
            condition = append(condition, false)
        }
    }
    return condition
}
