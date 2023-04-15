class SwitchWithYield {
    enum Day {
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
    }

    public String calculate(Day d) {
        return switch (d) {
            case SATURDAY, SUNDAY -> "week-end";
                default -> {
                    int remainingWorkDays = 5 - d.ordinal();
                    yield remainingWorkDays;
                }
            };
    }

    public String convertToLabel(int quarter) {
        String quarterLabel =
            switch (quarter) {
                case 0  -> {
                    System.out.println("Q1 - Winter");
                    yield "Q1 - Winter";
                };
                default -> "Unknown quarter";
            };
        return quarterLabel;
    }

    public String convertToLabel2(int quarter) {
            
        return switch (quarter) {
                case 0  -> {
                    System.out.println("Q1 - Winter");
                    yield "Q1 - Winter";
                };
                default -> "Unknown quarter";
        };
    }

}