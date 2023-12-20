func canPlaceFlowers(flowerbed []int, n int) bool {
    newFB := make([]int, len(flowerbed)+2)
    newFB[0] = 0
    newFB[len(newFB)-1] = 0
    copy(newFB[1:len(newFB)-1], flowerbed)
    for i := 1; i < len(newFB)-1; i++ {
        if newFB[i] == 0 && newFB[i-1] == 0 && newFB[i+1] == 0 {
            newFB[i] = 1
            n--
        }
    }

    return n <= 0
}