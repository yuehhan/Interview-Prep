<<<<<<< HEAD
var isPalindrome = function(s) {
    s = s.replace(/[^0-9a-zA-Z]+/gmi,"");
    s = s.toLowerCase();
    var l = 0, r = s.length - 1;
    console.log(s);

    while(l<r) {
        if(s.charAt(l) != s.charAt(r)) {
            return false;
        }
        l++;
        r--;
    }
    return true;
=======
var isPalindrome = function(s) {
    s = s.replace(/[^0-9a-zA-Z]+/gmi,"");
    s = s.toLowerCase();
    var l = 0, r = s.length - 1;
    console.log(s);

    while(l<r) {
        if(s.charAt(l) != s.charAt(r)) {
            return false;
        }
        l++;
        r--;
    }
    return true;
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
};