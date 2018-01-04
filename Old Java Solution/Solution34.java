package array;

public class Solution34 {

	public int[] searchRange(int[] nums, int target) {
		int low=0;
		int high = nums.length-1;
		int mid = (low+high)/2;
		while(low<high){
			mid = (low+high)/2;
			if (target == nums[mid]) {
				break;
			}
			if(nums[mid]<target){
				low = mid+1;
			} else {
				high = mid - 1;
			}
		}
		int j=mid;
		int k=mid;
		while(nums[j-1]==target){
			if (j > 0) {
				j--;
			}
		}
		while(nums[k+1]==target){
			if (k < nums.length - 1) {
				k++;
			}
		}
		int[] a = {j,k};
		return a;
	}

	public static void main(String[] args){
		Solution34 s = new Solution34();
		int[] a = {5, 7, 7, 8, 8, 10};
		int[] r;
		int target = 8;
		r=s.searchRange(a, target);
		for(int i:r){
			System.out.println(i);}

	}
}
