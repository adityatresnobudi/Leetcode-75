func moveZeroes(nums []int) {
    for i, j:= 0, 0; i < len(nums); i++ {
        if nums[i] != 0 {
            nums[j], nums[i] = nums[i], nums[j]   
        }
        if nums[j] != 0 {
            j++
        }
    }
}
