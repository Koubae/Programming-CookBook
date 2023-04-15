List<City> cities = List.of();

Map<State, Long> numberOfCitiesPerState =
    cities.stream()
          .collect(Collectors.groupingBy(
                   City::state, Collectors.counting()
          ));


Map.Entry<State, Long> stateWithTheMostCities =
    numberOfCitiesPerState.entrySet().stream()
                          .max(Map.Entry.comparingByValue())
                          .orElseThrow();


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
