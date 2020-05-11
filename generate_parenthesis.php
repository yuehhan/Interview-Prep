<!-- Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. -->
<?php 
class Solution {
    
    public $result = [];
    function generateParenthesis($n) {
        $this->backtracking('', $n, $n);
        return $this->result;
    }
    
    function backtracking($current, $left, $right) {
        if ($right == 0) { 
            array_push($this->result, $current);
        }
        if ($left > 0 && $right > 0) {
            $this->backtracking($current . '(', $left - 1, $right); 
        }
        if ($right > $left) { 
            $this->backtracking($current . ')', $left, $right - 1); 
        }
    }
}
?>