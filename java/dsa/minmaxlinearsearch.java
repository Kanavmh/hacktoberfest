import java.util.Scanner;

public class linearsearchminmax {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter number of entries:");
        int x = scanner.nextInt();
        int[] nums = new int[x];
        
        for(int i=0; i<x;i++){
            System.out.println("Enter number:");
            nums[i] = scanner.nextInt();
        }

        int minIndex = findMinIndex(nums);
        int maxIndex = findMaxIndex(nums);

        if(minIndex != -1){
            System.out.println("Minimum element found at index: " + minIndex + " and the number is: " + nums[minIndex]);
        }else{
            System.out.println("Array is empty");
        }

        if(maxIndex != -1){
            System.out.println("Maximum element found at index: " + maxIndex + " and the number is: " + nums[maxIndex]);
        }else{
            System.out.println("Array is empty");
        }
    }

    public static int findMinIndex(int[] nums) { //linear search 1
        if (nums.length == 0) return -1;
        int minIndex = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < nums[minIndex]) {
                minIndex = i;
            }
        }
        return minIndex;
    }

    public static int findMaxIndex(int[] nums) { //linear search 2
        if (nums.length == 0) return -1;
        int maxIndex = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }
}
