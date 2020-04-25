<?php 
    function isValid($s) {
        if(!$s) return true;

        $length = strlen($s);
        $stack = [];
        $hash = ['{'=>'}', '['=>']', '('=>')'];
        for($i=0; $i<$length; $i++){
            if(isset($hash[$s[$i]])){
                array_push($stack, $s[$i]);
            }elseif(empty($stack)){
                return false;
            }elseif($hash[array_pop($stack)]!=$s[$i]){
                return false;
            }
        }
        return empty($stack);
    }




?>