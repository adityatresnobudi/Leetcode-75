func increasingTriplet(nums []int) bool {
    first, second := math.MaxInt, math.MaxInt
    for _, num := range nums {
        if num <= first {
            first = num
            continue
        }

        if num <= second {
            second = num
            continue
        }

        return true
    }

    return false
}