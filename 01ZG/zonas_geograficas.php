<?php
    try{
        $command = escapeshellcmd('python run.py');
        $output = shell_exec($command);
        var_dump(http_response_code(400));
    }
    catch(Exception $e){
        var_dump(http_response_code(400));
        die(404);
    }
?>