public class MainRecords {
    public static void main(String[] args) {
        Person johnDoe = new Person("John", "Doe", 32, 364987565, "john.doe@example.com");

        System.out.printf("John => %s\n", johnDoe);

        Employee johnDoeEmployee = new Employee(johnDoe, 1);
        System.out.printf("Employee %s => %s\n", johnDoeEmployee.person().name(), johnDoeEmployee);

        try {
            new Employee(johnDoe, 0);
        } catch (IllegalArgumentException e) {
            System.err.printf("Employee record correctly thrown error -> %s\n", e);
        }

    }
}

record Person(String name, String surname, int age, int phoneNumber, String email) {}
record Employee(Person person, int employeeId) {
   public Employee {
    if (employeeId <= 0) {
        throw new IllegalArgumentException(String.format("employeeId must be equal or greater than 1, passed %d", employeeId));
    }
   } 
}