int myAtoi(char* str) {
    // printf("INT_MAX: %d",INT_MAX + 1);
    int l = strlen(str);
    int result = 0;
    int sign = 1;
    int i = 0;
    
    while (i < l){
        if (str[i] == ' '){
            i++;
            continue;
        }
        else{
            break;
        }
    }
    if (str[i] == '-'){
        sign = -1;
        i++;
    }
    else if(str[i] == '+'){
        i++;
    }
        
    while (i < l){
        if ((str[i] >= '0') && (str[i] <= '9')){
            if (((sign == 1) && (result > INT_MAX / 10)) || ((sign == 1) && (result == INT_MAX / 10) && str[i] > '7')){
                return INT_MAX
            }
            else if (((sign == -1) && (result > INT_MAX / 10)) || ((sign == -1) && (result == INT_MAX / 10) && str[i] > '8')){
                return INT_MIN 
            }
            
            result = result * 10 + str[i] - '0';
        }
        else{
            i = l;
        }
        i++;
    }
    
    if (sign == -1){
        result *= -1;
    }
    return result;
    
}