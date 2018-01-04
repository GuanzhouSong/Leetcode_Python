package array;

public class Solution31 {
	public int[] nextPermutation(int[] nums) {
		int i=nums.length-1;
		for(;i>=1;i--){
	         if(nums[i]>nums[i-1]){ 
	             break;
	         }
	      }
		
		//swap
		 if(i!=0){
			 for(int j = nums.length-1;j>i;j--){
		            if(nums[j]>nums[i]){
		                int t = nums[j];
		                nums[j] = nums[i];
		                nums[i] = t;
		                break;
		            }
		        }
		 }
		 
		 // reverse
		 int first = i;
	        int last = nums.length-1;
	        while(first<last){
	            int t = nums[first];
	            nums[first] = nums[last];
	            nums[last] = t;
	            first ++;
	            last --;
	        }
	        return nums;
        
    }
	
	public static void main(String[] args){
		Solution31 s = new Solution31();
		int[] a = {1,2};
		int target = 0;
		a = s.nextPermutation(a);
		for(int i:a){
		System.out.println(i);}
		
	}
}
