func hasDuplicate(nums []int) bool {
    seen := make(map[int] bool)
    for _, num := range nums {
        seen[num] = true
    } 
    return len(seen) < len(nums)
}
