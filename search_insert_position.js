// Insert the target number into the array
var searchInsert = function(nums, target) {
    let index =  nums.length;
    for(i=0; i<nums.length; i++){
        if(nums[i] == target || nums[i] > target){
            index = i;
            break;
        }
    }
    return index
};
