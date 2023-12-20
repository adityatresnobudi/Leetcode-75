func maxCandies(candies []int) int {
    max := 0
    for _, v := range candies {
        if max < v {
            v = max
        }
    }
    return max
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
    condition := make([]bool, len(candies))
    for i := 0; i < len(candies); i++ {
        if candies[i] + extraCandies >= maxCandies(candies) {
            condition[i] = true
            continue
        }
        condition[i] = false
    }
    
    return condition
}
