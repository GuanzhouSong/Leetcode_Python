package array;

public class Solution26 {
	public int removeDuplicates(int[] nums) {
       if (nums.length<2) return 0;
       int j = 0;
       for(int i =0;i<nums.length;i++){
    	   if(nums[i]!=nums[j]) nums[++j]=nums[i];
       }
       return j+1;
    }
	
	public static void main(String[] args){
		Solution26 s = new Solution26();
		int[] a = {0, 0, 0, 1, 2, 2};
		int target = 0;
		System.out.println(s.removeDuplicates(a));
	}
}
