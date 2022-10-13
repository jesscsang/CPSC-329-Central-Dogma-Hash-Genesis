import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.lang.Math;
import java.util.stream.Collectors;

public class hash {
    static ArrayList<String> ascii_list = new ArrayList<String>();
    static ArrayList<Double> math_list = new ArrayList<Double>();
    static ArrayList<Integer> mod_list = new ArrayList<Integer>();

    ///////////////////begin main method///////////////////
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter string: ");
        String input = scanner.nextLine(); // get user input

        for(int i = 0; i < input.length(); i++){ // turn every character in password to ascii value
            int ascii = (int) input.charAt(i);
            ascii_list.add(String.valueOf(ascii)); // add ascii values to ascii_list
        }
        for(int i = 0; i < ascii_list.size(); i++){ // for every value in ascii_list
            math(ascii_list.get(i)); // run hash method below with ascii value
        }

        mod(); // run mod method
        sort(); // run sort method
    }
    ///////////////////end main method///////////////////

    ///////////////////begin math method///////////////////
    public static void math(String input){ // hash method
        ArrayList<String> individual = new ArrayList<String>(); // define individual list where each ascii value will be split to individual characters
        individual.clear(); // make sure that the list is empty

        for(int i = 0; i< input.length(); i++){ // for every value in individual list
            individual.add(String.valueOf(input.charAt(i)));
            // add value to list. Example: ascii_list -> [104, 105] -----> output two individual lists
            // the first is [1, 0, 4] and the second is [1, 0, 5]
        }

        if(individual.size() == 3){ // if the individual list has a length of 3 (I did this because some ascii values will have an individual list that is made up of only two indices. could write an else if later on)
            int l0 = Integer.parseInt(individual.get(0)); // l0 is the first index in the individual list
            int l1 = Integer.parseInt(individual.get(1)); // l1 is the second index in the individual list
            int l2 = Integer.parseInt(individual.get(2)); // l2 is the third index in the individual list
            // below is just math which will be put in variable "hash"
            int hash = (int) (((Math.pow(l0 + individual.size(), 10) + Math.pow(l1 + individual.size(), 10)) / (individual.size())) / (l2 * individual.size()));

            double finale; // initiate variable finale
            finale = Math.pow(hash, 3); // finale is hash^3
            math_list.add(finale); // add the finale number to math_list
        }
    }
    ///////////////////End math method///////////////////

    ///////////////////begin mod method///////////////////
    public static void mod(){
        for(int i = 0; i < math_list.size(); i++){ // for all the values in math list
            double mod_value = math_list.get(i) % 10000; // get the four most digits on the right of the value
            mod_list.add((int) mod_value); // add that value to mod_list
        }
    }
    ///////////////////end mod method///////////////////

    ///////////////////begin sort method///////////////////
    public static void sort(){
        List<Integer> sortedList = mod_list.stream().sorted().collect(Collectors.toList()); // sort the mod_list from in ascending order
        String sortedString = ""; // empty string which we will append to
        for(int i = 0; i < sortedList.size(); i++){ // for every value in assorted_list
            sortedString = sortedString + sortedList.get(i); // append value to sortedString
        }

        System.out.println("output " + sortedString); // print finale output
    }
    ///////////////////end sort method///////////////////
}
