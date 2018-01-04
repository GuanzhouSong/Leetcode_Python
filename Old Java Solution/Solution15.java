package array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Solution15 {

	public List<List<Integer>> threeSum(int[] nums) {
		Arrays.sort(nums);
		int target=0;
		List<List<Integer>> result = new ArrayList<List<Integer>>();
		for(int i = 0;i<nums.length;i++){
			target = (-1)*nums[i];
			HashMap<Integer, Integer> map = new HashMap<>();
			for(int j=0;j<nums.length;j++){
				if(j==i) break;
				if(map.containsKey(target-nums[j])){
					ArrayList<Integer> r = new ArrayList<>();
					r.add(nums[i]);
					r.add(nums[j]);
					r.add(target-nums[j]);
					result.add(r);
				}
				map.put(nums[j], j);
			}
		}
		return result;
	}

	public static void main(String[] args){
		Solution15 solution = new Solution15();
		int[] nums = {-1,0,1,2,-1,-4};
		System.out.println(solution.threeSum(nums));
	}
}