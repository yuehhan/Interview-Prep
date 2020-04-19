// Check if an integer is a palindrome
var isPalindrome = function(x) {
    if(x<0) return false;
    if(x<10) return true;
    let string = x.toString()
    let left = 0
    let right = string.length-1
    while(left<right){
        if(string[left] === string[right]){
            left+=1
            right -=1
        }else{
            return false
        };
    };
    return true
}
