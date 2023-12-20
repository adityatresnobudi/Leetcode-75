// iterate forward using prefix and backward using postfix
// first iteration -> res = 1, 1, 2*1 , 3*2*1
// second iteration -> res = 2*3*4, 1*3*4, 2*1*4, 3*2*1*1

func productExceptSelf(nums []int) []int {
    res := make([]int, len(nums))

    prefix := 1
    for idx, num := range nums {
        res[idx] = prefix
        prefix *= num
    }

    postfix := 1
    for i := len(nums)-1; i >= 0; i-- {
        res[i] *= postfix
        postfix *= nums[i]
    }
    return res
}
