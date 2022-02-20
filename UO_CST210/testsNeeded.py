def tN(s):	
    '''(str) -> int '''
    
    if len(s) != 0:
        prev_char = s[0]
        dup_ct = 1
        high_ct = 1
    else:
        high_ct = 0
        dup_ct = 0



        
    for i in range(1, len(s)):
        
        if s[i] == prev_char:					
            dup_ct += 1
            
    
        else:
            prev_char = s[i]
            
            if dup_ct > high_ct:
                 high_ct = dup_ct
            dup_ct = 1
            
        
            
            
    return high_ct
    
