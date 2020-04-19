// Given an array nums and a value val, remove all instances of that value in-place and return the new length.
var removeElement = function(nums, val) {
    let left = 0
    let right = nums.length-1
    while(left <= right){
        if(nums[right] === val){
            right -=1
        }else if(nums[left] === val){
            [nums[left], nums[right]] = [nums[right], nums[left]]
            left+=1
        }else{
            left += 1
        }
    }
    return nums.slice(0,right+1).length
};  