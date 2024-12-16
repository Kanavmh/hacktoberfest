import java.util.Scanner;

public class selectionsort {
    public static void selectionSort(int[] arr){
        for(int i =0; i<arr.length -1; i++){
            int minIndex =i;
            for(int j=i+1; j<arr.length;j++){
                if(arr[j]<arr[minIndex]){
                    minIndex = j;
                }
            }
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;

        }

    }

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array: ");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements of the array: ");
        for(int i=0;i<n;i++){
            arr[i] = scanner.nextInt();
        }
        scanner.close();
        //int[] arr1 = {64,25,12,22,11};

        
        selectionSort(arr);
        for(int i =0; i<arr.length; i++){
            System.out.print(arr[i] + " ");
        }
    }
}
