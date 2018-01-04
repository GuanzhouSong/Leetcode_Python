package array;

public class Solution27 {

	public int removeElement(int[] nums, int val) {
		int j = 0;
		for(int i=0;i<nums.length;i++){
			if(nums[i]!=val)nums[j++]=nums[i];
		}
		return j;
	}

	public static void main(String[] args){
		Solution27 s = new Solution27();
		int[] a = {0, 0, 0, 1, 2, 2,2,0,5,8,0};
		int target = 0;
		System.out.println(s.removeElement(a, 0));
	}
}
