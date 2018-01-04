package array;

import java.util.Arrays;

public class Solution16 {
	public int threeSumClosest(int[] nums, int target) {
        int min = Integer.MAX_VALUE;
        Arrays.sort(nums);
        int result =0;
        int i = 0;
        while(i<nums.length-2){
        	int j = i+1;
        	int k = nums.length-1;
        	while(j<k){
        		int sum = nums[i] + nums[j] + nums[k];
        		if(min>Math.abs(target-sum)) {
        			result = sum;
        			min = Math.abs(target-sum);
        		}
        		if(sum<=target) j++;
            	if(sum>=target) k--;
        	}
        	i++;
        }
        return result;
    }
	
	public static void main(String[] args){
		Solution16 s = new Solution16();
		int[] a = {1,1,1,0};
		int target = 100;
		System.out.println(s.threeSumClosest(a, target));
	}
}
