// Check if string of parentheses is valid, using stacks
var isValid = function(s) {
    const isPair = function(left, right){
    if(left === '(' && right === ')'){
        return true
    }else if(left === '[' && right === ']'){
        return true
    }else if(left==='{' && right==='}'){
        return true
    }else{
        return false
    }
    }
    let stack = []
    for(i=0; i<s.length; i++){
        if(stack.length && isPair(stack[stack.length-1], s[i])){
            stack.pop()
        }else{
            stack.push(s[i])
        }
    }
    return stack.length === 0;
}