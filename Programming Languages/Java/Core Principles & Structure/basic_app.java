/**
 * Simple App representing how a Java App would run in most simple form and 
 * relation of the 'Main' Class app and other app classes
 * @docs https://docs.oracle.com/javase/tutorial/java/concepts/class.html
 * --- BUILD 
 * javac basic_app.java
 * 
 * --- RUN 
 * 
 * java BasicApp
 */



// Write and implement an interface 
interface BicycleInterface {
    //  wheel revolutions per minute
    void changeCadence(int newValue);

    void changeGear(int newValue);

    void speedUp(int increment);

    void applyBrakes(int decrement);
}

class ACMEBicycle implements BicycleInterface {

    int cadence = 0;
    int speed = 0;
    int gear = 1;

   // The compiler will now require that methods
   // changeCadence, changeGear, speedUp, and applyBrakes
   // all be implemented. Compilation will fail if those
   // methods are missing from this class.

    public void changeCadence(int newValue) {
        cadence = newValue;
    }

    public void changeGear(int newValue) {
        gear = newValue;
    }

    public void speedUp(int increment) {
        speed = speed + increment;   
    }

    public void applyBrakes(int decrement) {
        speed = speed - decrement;
    }

    public void printStates() {
        System.out.println("cadence:" +
            cadence + " speed:" + 
            speed + " gear:" + gear);
    }
}


class Bicycle {

    int cadence = 0;
    int speed = 0;
    int gear = 0;

    void changeCadance(int value) {
        cadence = value;
    }

    void changeGear(int value) {
        gear = value;
    }

    void speedUp(int increment) {
        speed = speed + increment;
    }

    void breaks(int decrement) {
        speed = speed - decrement;
    }

    void printStates() {
        System.out.println("cadence:" + cadence + 
        " speed:" + speed + 
        " gear:" + gear
        );
    }

}


class BasicApp {

    public static void main(String[] args)  {

         // Create two different 
        // Bicycle objects
        Bicycle bike1 = new Bicycle();
        Bicycle bike2 = new Bicycle();

        // Invoke methods on 
        // those objects
        bike1.changeCadance(50);
        bike1.speedUp(10);
        bike1.changeGear(2);
        bike1.printStates();

        bike2.changeCadance(50);
        bike2.speedUp(10);
        bike2.changeGear(2);
        bike2.changeCadance(40);
        bike2.speedUp(10);
        bike2.changeGear(3);
        bike2.printStates();
    }
}


