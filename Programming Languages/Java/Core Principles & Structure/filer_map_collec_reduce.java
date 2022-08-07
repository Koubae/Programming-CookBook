public // @docs https://developer.ibm.com/tutorials/java-language-constructs-2/
import java.math.BigDecimal;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Person {

    Person() {

    }

    public static <K, T> K getEyeColor(T t) {
        Map<String, List<Person>> map = Map();
        return map;
    }
}

interface SomeInterface {

}

class Employee extends Person implements SomeInterface {

    Employee() {

    }

    public String getEyeColor() {
        return new String();
    }

    public <R> R getSalary() {
    }
}

class Manager extends Person implements SomeInterface {

    Manager() {

    }

    public static Manager promote(Employee employee) {
        return new Manager();
    }
}


class Main {

    Main() {

    }

    public static void main(String[] args) {
        //
    }

    // Use Filter
    public List<Person> filterBonusEligible(final List<Person> people) {
        return people
                .stream()
                .filter(person -> person instanceof SomeInterface)
                .collect(Collectors.toList());
    }

    // Use Map
    public List<Manager> mapManager(final List<Person> people) {
        return people
                .stream()
                .filter(person -> person instanceof Manager)
                .map(person -> (Manager)person)
                .collect(Collectors.toList());
    }

    public List<Manager> promoteBlueEyedEmployeesToManager(final List<Employee> employees) {
        return employees
                .stream()
                .filter(employee -> employee.getEyeColor().equalsIgnoreCase("BLUE"))
                .map(Manager::promote)
                .collect(Collectors.toList());
    }
    
    // Collect 
    public Map<String, List<Person>> collectByEyeColor(final List<Person> people) {
        return people
                .stream()
                .collect(Collectors.groupingBy(Person::getEyeColor));
    }
    
    // Reduce
    public BigDecimal computeTotalPayroll(final List<Employee> employees) {
        return employees
                .stream()
                .map(Employee::getSalary)
                .reduce(BigDecimal.ZERO, (current, value) -> current.add(value));
    }
} filer_map_collec_reduce {
    
}
