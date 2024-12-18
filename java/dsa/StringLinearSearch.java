public class searchforstring {
    public static void main(String[] args) {
        
        String names[] = {"Arun", "Patel", "Nitasha", "Kashish","Aruni","Nupur","Samya","Shobita","Sehaj","Chirag","Tanya","Nandu","Ayakshi"};
        String target = "Aruni";

        int result = linearSearch(names, target);

        if(result != -1){
            System.out.println("Element found at index: " + result);   
        }else{
            System.out.println("Element not found in the array");
        } 
    }

    public static int linearSearch(String[] names, String target){
        for(int i=0;i< names.length;i++){
            if(names[i].equals(target)){
                return i;
            }
        }
        return -1;
    }
}
