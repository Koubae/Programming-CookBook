import java.util.UUID;

public class MainStack {
    public static void main(String[] args) {
        
        Stack stack = new Stack();
        int lastIndex = 0;
        for (int i = 0; i < 11; i++) {
            stack.add(String.format("%d -- %s", i + 1, UUID.randomUUID().toString()));
            lastIndex = i;
        }

        int i = 0;
        for (String element: stack.getStack()) {
            System.out.printf("- [%d] Element -> %s\n", i, element);
            i ++;
        }

        System.out.println("----------------- GET ELEMENTS FROM STACK --------------");
        for (int y = 0; y < 20; y ++ ) {
            System.out.printf("- [%d] {%d} Next Stack: %s\n", y + 1, stack.getStackScanPosition(), stack.getNextOnStack());
        }

        System.out.println("----------------- ADD ELEMENTS into STACK --------------");
        
        lastIndex ++;
        for (int y = 0; y < 3; y++) {
            lastIndex ++;
            String element = String.format("%d -- %s", lastIndex, UUID.randomUUID().toString());
            System.out.printf("Adding element %s\n",  element);
            stack.add(element);
        }


        System.out.println("----------------- PRINT ALL ELEMENTS --------------");

        i = 0;
        for (String element: stack.getStack()) {
            System.out.printf("- [%d] Element -> %s\n", i, element);
            i ++;
        }

        System.out.println("----------------- GET ELEMENTS FROM STACK --------------");

        for (int y = 0; y < 20; y ++ ) {
            System.out.printf("- [%d] {%d} Next Stack: %s\n", y, stack.getStackScanPosition(), stack.getNextOnStack());
        }


        System.out.println("----------------- Let's play now with a very small stack with only 2 capacity! --------------");
        Stack minIStack = new Stack(2);
        lastIndex = 0;
        for (int y = 0; y < 11; y++) {
            minIStack.add(String.format("%d -- %s", y + 1, UUID.randomUUID().toString()));
            lastIndex = y;
        }
        System.out.println("----------------- GET ELEMENTS FROM MINI STACK --------------");
        for (int y = 0; y < 20; y ++ ) {
            System.out.printf("- [%d] {%d} Next Stack: %s\n", y + 1, minIStack.getStackScanPosition(), minIStack.getNextOnStack());
        }


        System.out.println("----------------- Let's Check with a stack that is not yet full! --------------");
        Stack stackDemo2 = new Stack();
        
        System.out.println(String.format("stack top -> %s", stackDemo2.top()));
        System.out.println(String.format("stack bottom -> %s", stackDemo2.bottom()));
        System.out.println(String.format("stack next on stack %d -> %s", stackDemo2.getStackScanPosition(), stackDemo2.getNextOnStack()));

        stackDemo2.add("Element 1");
        System.out.println(String.format("stack bottom -> %s", stackDemo2.bottom()));

        stackDemo2.add("Element 2");
        System.out.println(String.format("stack bottom -> %s", stackDemo2.bottom()));

        stackDemo2.add("Element 3");
        System.out.println(String.format("stack bottom -> %s", stackDemo2.bottom()));

        for (int y = 0; y < 10; y++ ){
            String element = stackDemo2.getNextOnStack();
            int scanPosition = stackDemo2.getStackScanPosition();
            System.out.println(String.format("stack next on stack %d -> %s", scanPosition, element));
        }

    }

    

    
}


/**
 *
 * Minimalistic Stack implementation
 * It uses an index as 'cursor' to identify the current latest element added in the stack (therefore being at the top of the stack)
 * <p></p>
 * We can go through the stack via <strong><code>getNextOnStack</code></strong> method which automatically wrap back up to the top element,
 * and is doing this by simply going backward from the current index
 *
 * @see <a href="https://stackoverflow.com/a/15840632/13903942">Credit: Java Stack with elements limit<a>
 * @credit <a href="https://stackoverflow.com/users/150016/tom">Tom<a>
 */
class Stack {
    private static final int STACK_DEFAULT_SIZE = 10;
    private static final int STACK_MAX_SIZE = 1000;

    private final int size;
    private final String[] stack;
    
    private int index = 0;
    private int stackScanPosition = 0;

    public Stack() {
        size = STACK_DEFAULT_SIZE;
        stack = new String[size];
    }

    public Stack(int maxSize) throws IllegalArgumentException {
        if (maxSize <= 0 || maxSize > STACK_MAX_SIZE) {
            throw new IllegalArgumentException(String.format("Max size must be between 0 and %d, %s provided", STACK_MAX_SIZE, maxSize));
        }
        this.size = maxSize;
        stack = new String[size];
    }

    public void add(String element) {
        indexWrap();
        stack[index] = element;
        stackScanPosition = index; // when adding a new element, the stackScanPosition reset. This can be changed depending on use case
        index ++;
    }

    /**
     * Will scan the current stack backwards returning current elements
     * If the index position of the scan is over 0 than it wraps back to the max limit of the stack
     * i.e:
     * <pre><code>
     *     Given a stack of size 10 and currently only 4 elements, that's how it would look getting the stack one by one
     *
     *                |
     *      {a, b, c, d, null, null, null, null, null, null}
     *             |
     *      {a, b, c, d, null, null, null, null, null, null}
     *          |
     *      {a, b, c, d, null, null, null, null, null, null}
     *       |
     *      {a, b, c, d, null, null, null, null, null, null}
     *                |  <--- It reset to the current index, if a null is encountered than the stack must not be full ;)
     *      {a, b, c, d, null, null, null, null, null, null}
     *             |
     *      {a, b, c, d, null, null, null, null, null, null}
     *          |
     *      {a, b, c, d, null, null, null, null, null, null}
     * </code></pre>
     * 
     * @return String
    */
    public String getNextOnStack() {
        String element = accessStack(stackScanPosition);
        if (element == null) {
            stackScanPosition = getIndex();
            element = accessStack(stackScanPosition);
        }

        stackScanPosition --;
        stackScanPositionWrap(); 
        return element;
    }

    public String top() {
        return accessStack(getIndex());
    }

    public String bottom() {
        String element = accessStack(index);
        if (element == null)
            element = accessStack(0);
        return element;
    }

    public String[] getStack() {
        return stack;
    }

    public int getIndex() {
        return index - 1;
    }

    public int getStackScanPosition() {
        return stackScanPosition;
    }

    private void indexWrap() {
        if (index + 1 > size)
            index = 0;
    }

    private void stackScanPositionWrap() {
        if (stackScanPosition < 0) {
            stackScanPosition = size - 1;
        }
    }

    private String accessStack(int position) {
        try {
            return stack[position];
        } catch (ArrayIndexOutOfBoundsException ignored) {
            return null;
        }
    }
        
}