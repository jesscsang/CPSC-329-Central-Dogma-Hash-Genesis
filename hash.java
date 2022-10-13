import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.lang.Math;
import java.util.stream.Collectors;


public class hash {
    static ArrayList<Double> finaleboy = new ArrayList<Double>();
    static ArrayList<Integer> finaleboy2 = new ArrayList<Integer>();
    static String finaleoffinale = "";
    public static void main(String[] args){
        ArrayList<String> list = new ArrayList<String>();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter string: ");
        String input = scanner.nextLine();

        for(int i = 0; i < input.length(); i++){
            int ascii = (int) input.charAt(i);
            list.add(String.valueOf(ascii));
        }


        for(int i = 0; i < list.size(); i++){
            hash(list.get(i));
        }

        convertToHex();

        sort();
    }

    public static void hash(String input){
        ArrayList<String> list1 = new ArrayList<String>();
        list1.clear();

        for(int i = 0; i< input.length(); i++){
            list1.add(String.valueOf(input.charAt(i)));
        }

        System.out.println(list1);

        if(list1.size() == 3){
            int l0 = Integer.parseInt(list1.get(0));
            System.out.println("l0 is " + l0);
            int l1 = Integer.parseInt(list1.get(1));
            System.out.println("l1 is " + l1);
            int l2 = Integer.parseInt(list1.get(2));
            System.out.println("l2 is " + l2);
            int hash = (int) (((Math.pow(l0 + list1.size(), 10) + Math.pow(l1 + list1.size(), 10)) / (list1.size())) / (l2 * list1.size()));
            System.out.println("hash is " + hash);
            System.out.println("huh? " + hash);

            double finale;
            finale = Math.pow(hash, 3);
            finaleboy.add(finale);
            System.out.println("finaleboy " + finaleboy);

        }
    }

    public static void convertToHex(){
        for(int i = 0; i < finaleboy.size(); i++){
            double hi = finaleboy.get(i) % 10000;
            finaleboy2.add((int) hi);
        }

        System.out.println("ladies and gentlemen " + finaleboy2);


        for(int i = 0; i < finaleboy2.size(); i++){
            finaleoffinale = finaleoffinale + finaleboy2.get(i);
        }

        System.out.println("serious finale " + finaleoffinale);
    }


    public static void sort(){
        System.out.println("ok so we have " + finaleboy2);

        List<Integer> sortedList = finaleboy2.stream().sorted().collect(Collectors.toList());
        System.out.println(sortedList);

        String sortedfinale = "";
        for(int i = 0; i < sortedList.size(); i++){
            sortedfinale = sortedfinale + sortedList.get(i);
        }

        System.out.println("output " + sortedfinale);
    }



}
