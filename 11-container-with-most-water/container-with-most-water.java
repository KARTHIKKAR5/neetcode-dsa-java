class Solution {
    public int maxArea(int[] height) {
        int L = 0;
        int R = height.length - 1;
        int bestoutput =0;

        while (L < R ){
            int currentArea = (R - L) * Math.min(height[L], height[R]);

            if(currentArea > bestoutput){
                bestoutput = currentArea;

            }
            if(height[L] < height[R] ){
                L++;
            }
            else if (height[R] < height[L]){
                R--;
            }
            else if(height[L] == height[R]){

                L++;

            }

            
            

        }
        return bestoutput;

        
        
    }
}