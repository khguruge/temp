class Selection{

    public static int search ( int arr[] , int x){
        int n = arr.length;
        for (int i = 0 ; i < n ; i++){
            if ( arr[i]==x){
                return i;
            }
        }
        return -1;
    }
    
    public static void main(String args[]) {
        int arr[] = { 2,3,4,6,7,23,4};
        int x = 4;
        int result = search(arr , x);
        System.out.print("\n" + "Index is " + result + "\n\n" );
    }

}