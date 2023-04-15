// https://dev.java/learn/records/

public record Point(int x, int y) {}


/*
- 1 Immutable class with 2 fields, x, y (int)
- 2 Has canonical constructor 
- 3 toString(), equals(), hashCode() are implemented by the compiler
- 4 Can implement Serializable interface, to send instance via file-sytem/network

*/


// Compact constructor
public record Range(int start, int end) {

    public Range {
        // set negative start and end to 0
        // by reassigning the compact constructor's
        // implicit parameters
        if (start < 0)
            start = 0;
        if (end < 0)
            end = 0;
    }

}



// Using Canonical Constructor
public record Range(int start, int end) {

    public Range(int start, int end) {
        if (end <= start) {
            throw new IllegalArgumentException("End cannot be lesser than start");
        }
        if (start < 0) {
            this.start = 0;
        } else {
            this.start = start;
        }
        if (end > 100) {
            this.end = 10;
        } else {
            this.end = end;
        }
    }
}

// Defining any Constructor
public record State(String name, String capitalCity, List<String> cities) {

    public State {
        // List.copyOf returns an unmodifiable copy,
        // so the list assigned to `cities` can't change anymore
        cities = List.copyOf(cities);
    }

    public State(String name, String capitalCity) {
        this(name, capitalCity, List.of());
    }

    public State(String name, String capitalCity, String... cities) {
        this(name, capitalCity, List.of(cities));
    }

}

// Using Records in a Real Use Case
record NumberOfCitiesPerState(State state, long numberOfCities) {

    public NumberOfCitiesPerState(Map.Entry<State, Long> entry) {
        this(entry.getKey(), entry.getValue());
    }

    public static Comparator<NumberOfCitiesPerState> comparingByNumberOfCities() {
        return Comparator.comparing(NumberOfCitiesPerState::numberOfCities);
    }
}

NumberOfCitiesPerState stateWithTheMostCities =
    numberOfCitiesPerState.entrySet().stream()
                          .map(NumberOfCitiesPerState::new)
                          .max(NumberOfCitiesPerState.comparingByNumberOfCities())
                          .orElseThrow();
