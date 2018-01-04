package array;

public class Solution33 {

  public int search(int[] nums, int target) {
    int low = 0;
    int high = nums.length-1;
    int forward = (low+high)/2;
    while(low<high){
      forward = (low+high)/2;
      if(nums[forward]>nums[high]){
        low = forward + 1;
      }else high = forward;
    }
    int ro = forward;
    int realmid;
    low = 0;
    high = nums.length-1;
    while(low<=high){
      int mid=(low+high)/2;
      realmid=(mid+ro)%nums.length;
      if(nums[realmid]==target)return realmid;
      if(nums[realmid]<target)low=mid+1;
      else high=mid-1;
    }
    return -1;
  }
}
