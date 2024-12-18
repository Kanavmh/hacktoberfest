public class linearvsbinary {
    public static void main(String[] args){
        int nums[] = {1,2,3,5,7,9,23,53};
        int target = 9;

        int result1 = linearSearch(nums, target);
        int result2 = binarySearch(nums, target);
//binary is better since it takes less steps to find the target
        if(result1 != -1){
            System.out.println("Element found at index: " + result1);
        }else{
            System.out.println("Element not found in the array");
        }

        if(result2 != -1){
            System.out.println("Element found at index: " + result1);
        }else{
            System.out.println("Element not found in the array");
        }
    }

    public static int linearSearch(int[] nums, int target){
        int steps =0;
        for(int i=0; i<nums.length;i++){
            steps++;
            if(nums[i] == target){
                System.out.println("Steps taken by linear: " + steps);
                return i;
            }
        }
        System.out.println("Steps taken by linear: " + steps);
        return -1;
    }

    public static int binarySearch(int[] nums, int target){
        int steps =0;
        int left =0;
        int right = nums.length-1;

        while(left <= right){
            steps++;
            int mid = (left+right)/2;

            if(nums[mid] == target){
                System.out.println("Steps taken by binary: " + steps);
                return mid;
            }
            if(nums[mid] < target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return -1;
    }
    
}
