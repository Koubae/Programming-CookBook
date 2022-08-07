/**
 * Shadowing
 * @docs https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html Shadowing
 * 
 * If a declaration of a type (such as a member variable or a parameter name) in a particular scope (such as an inner class or a method definition)
 *  has the same name as another declaration in the enclosing scope, then the declaration shadows the declaration of the enclosing scope. 
 * You cannot refer to a shadowed declaration by its name alone.
 * --- BUILD 
 * 
 * @output
x = 23
this.x = 1
ShadowTest.this.x = 0
 */
class ShadowTest {

    public int x = 0;

    class FirstLevel {

        public int x = 1;

        void methodInFirstLevel(int x) {
            System.out.println("x = " + x);
            System.out.println("this.x = " + this.x);
            System.out.println("ShadowTest.this.x = " + ShadowTest.this.x);
        }
    }

    public static void main(String... args) {
        ShadowTest st = new ShadowTest();
        ShadowTest.FirstLevel fl = st.new FirstLevel();
        fl.methodInFirstLevel(23);
    }
}
