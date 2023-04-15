/**
 * Enum
 * @docs https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html

 * --- BUILD 
 * 
 * @output
Mondays are bad.
Midweek days are so-so.
Fridays are better.
Weekends are best.
Day is SUNDAY
Day is MONDAY
Day is TUESDAY
Day is WEDNESDAY
Day is THURSDAY
Day is FRIDAY
Day is SATURDAY
 */

enum Day {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY,
    THURSDAY, FRIDAY, SATURDAY 
}

class EnumTest {
    Day day;
    
    public EnumTest(Day day) {
        this.day = day;
    }
    
    public void tellItLikeItIs() {
        switch (day) {
            case MONDAY:
                System.out.println("Mondays are bad.");
                break;
                    
            case FRIDAY:
                System.out.println("Fridays are better.");
                break;

            case SATURDAY: case SUNDAY:
                System.out.println("Weekends are best.");
                break;
                        
            default:
                System.out.println("Midweek days are so-so.");
                break;
        }
    }
    
    public static void main(String[] args) {
        EnumTest firstDay = new EnumTest(Day.MONDAY);
        firstDay.tellItLikeItIs();
        EnumTest thirdDay = new EnumTest(Day.WEDNESDAY);
        thirdDay.tellItLikeItIs();
        EnumTest fifthDay = new EnumTest(Day.FRIDAY);
        fifthDay.tellItLikeItIs();
        EnumTest sixthDay = new EnumTest(Day.SATURDAY);
        sixthDay.tellItLikeItIs();
        EnumTest seventhDay = new EnumTest(Day.SUNDAY);
        // Use enum methid .values() to ierate through each value
        for (Day day : Day.values()) {
            System.out.printf("Day is %s\n", day);
        }
    }
}