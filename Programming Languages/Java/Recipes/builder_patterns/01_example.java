// https://stackoverflow.com/a/222295/13903942public class StudentBuilder
{
    private String _name;
    private int _age = 14;      // this has a default
    private String _motto = ""; // most students don't have one

    public StudentBuilder() { }

    public Student buildStudent()
    {
        return new Student(_name, _age, _motto);
    }

    public StudentBuilder name(String _name)
    {
        this._name = _name;
        return this;
    }

    public StudentBuilder age(int _age)
    {
        this._age = _age;
        return this;
    }

    public StudentBuilder motto(String _motto)
    {
        this._motto = _motto;
        return this;
    }
}

// code .. 
Student s1 = new StudentBuilder().name("Eli").buildStudent();
Student s2 = new StudentBuilder()
                 .name("Spicoli")
                 .age(16)
                 .motto("Aloha, Mr Hand")
                 .buildStudent();