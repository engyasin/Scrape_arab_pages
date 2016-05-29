def convert(wind56,wind_list = wind_list,utf8_list = utf8_list):
    # define the list of strings (arranged)
    equal_chars_list = str()
    for i,c in enumerate(wind56):
        m = wind_list.find(c)
        # we got m:
            
        equal_chars_list += utf8_list[2*m:2*m+2];
        
    print equal_chars_list      
    return(equal_chars_list)
