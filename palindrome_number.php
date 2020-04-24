<?php  
function isPalindrome($x) {
    $x = strval($x);
    $left = 0;
    $right = strlen($x)-1;
    while($left <= $right){
        if($x[$left] === $x[$right]){
            $left+=1;
            $right-=1;
        } else{
            return false;
        }
    }
    return true;
}
?>