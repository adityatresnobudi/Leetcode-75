func canPlaceFlowers(flowerbed []int, n int) bool {
    length := len(flowerbed)

    for idx, flower := range flowerbed {
        if length == 1 {
            if flower == 0 {
                flower = 1
                n--
                continue
            }
            break
        }
        
        switch idx {
        case 0:
            if flowerbed[idx+1] == 0 && flowerbed[idx] == 0 {
                flowerbed[idx] = 1
                n--
            }
        case length-1:
            if flowerbed[idx-1] == 0 && flowerbed[idx] == 0 {
                flowerbed[idx] = 1
                n--
            }
        default:
            if flowerbed[idx-1] == 0 && flowerbed[idx+1] == 0 && flowerbed[idx] == 0 {
                flowerbed[idx] = 1
                n--
            }
        }
    }

    return n <= 0
}