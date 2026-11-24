class Solution {
public:
    int addDigits(int num) {
        while (num >= 10) {
            int digSum = 0;

            while (num > 0) {
                int lastDig = num % 10;
                num = num / 10;
                digSum += lastDig;
            }

            num = digSum;
        }

        return num;
    }
}; 