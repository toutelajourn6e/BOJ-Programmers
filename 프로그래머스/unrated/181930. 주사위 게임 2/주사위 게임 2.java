class Solution {
    public int solution(int a, int b, int c) {
        if (a == b && b == c && a == c)
            return (a + b + c) * ((a * a) + (b * b) + (c * c)) * ((int)Math.pow(a, 3) + (int)Math.pow(b, 3) + (int)Math.pow(c , 3));
        else if (a != b && b != c && a != c)
            return a + b + c;
        else
            return (a + b + c) * ((a * a) + (b * b) + (c * c));
    }
}