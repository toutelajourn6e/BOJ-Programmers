class Solution {
    public String solution(String code) {
        String ret = "";
        boolean mode = false;
        
        for(int i=0; i < code.length(); i++){
            if (mode == false){
                if (code.charAt(i) == '1')
                    mode = true;
                else if (i % 2 == 0)
                    ret += code.charAt(i);
            }
            else{
                if (code.charAt(i) == '1')
                    mode = false;
                else if (i % 2 == 1)
                    ret += code.charAt(i);
            }
                
        }
        if (ret.equals(""))
            return "EMPTY";
        else
            return ret;
    }
}