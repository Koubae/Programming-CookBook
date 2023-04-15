public class BreakWithLabelDemo  {
    public static void main(String[] args) {
        int[][] data = {
            {
                32, 22, 66, 129, 923,
            },
            {
                234, 2342, 1233, 656, 342
            },
            {
                24, 123, 345345, 123, 435, 123245,
            }
        };        

        int target = 123;
        if (args.length >= 1) {
            try {
                target = Integer.valueOf(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("Error while converting input, reason: " + e);
            }
        }


        int i = 0; 
        int j = 0;
        boolean found = false;

    search:
        for (; i < data.length; i++) {
            for (; j < data[i].length; j++) {
                if (data[i][j] == target) {
                    found = true; 
                    break search;
                }
            }
        }

        if (found) {
            System.out.printf("Found %d at row %d and collumn %d\n", target, i+1, j+1);
        } else {
            System.out.printf("Target %d not found in data\n", target);
        }


    }
    
}
