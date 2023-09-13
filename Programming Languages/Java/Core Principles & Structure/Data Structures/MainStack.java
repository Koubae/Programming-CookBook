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
            System.out.printf("- [%d] {%d} Next Stack: %s\n", y + 1, stack.getStackScanPosition(), stack.stackDown());
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
            System.out.printf("- [%d] {%d} Next Stack: %s\n", y, stack.getStackScanPosition(), stack.stackDown());
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
            System.out.printf("- [%d] {%d} Next Stack: %s\n", y + 1, minIStack.getStackScanPosition(), minIStack.stackDown());
        }


        System.out.println("----------------- Let's Check with a stack that is not yet full! --------------");
        Stack stackDemo2 = new Stack();
        
        System.out.println(String.format("stack top -> %s", stackDemo2.top()));
        System.out.println(String.format("stack bottom -> %s", stackDemo2.bottom()));
        System.out.println(String.format("stack next on stack %d -> %s", stackDemo2.getStackScanPosition(), stackDemo2.stackDown()));

        stackDemo2.add("Element 1");
        System.out.println(String.format("stack bottom -> %s", stackDemo2.bottom()));

        stackDemo2.add("Element 2");
        System.out.println(String.format("stack bottom -> %s", stackDemo2.bottom()));

        stackDemo2.add("Element 3");
        System.out.println(String.format("stack bottom -> %s", stackDemo2.bottom()));

        stackDemo2.add("Element 4");
        System.out.println(String.format("stack bottom -> %s", stackDemo2.bottom()));
        
        i = 0;
        for (String element: stackDemo2.getStack()) {
            System.out.printf("- [%d] Element -> %s\n", i, element);
            i ++;
        }

        for (int y = 0; y < 10; y++ ){
            String element = stackDemo2.stackDown();
            int scanPosition = stackDemo2.getStackScanPosition();
            System.out.println(String.format("stack down on stack %d -> %s", scanPosition, element));
        }

        System.out.println("----------------- Stack up! --------------");
        for (int y = 0; y < 10; y++ ){
            String element = stackDemo2.stackUp();
            int scanPosition = stackDemo2.getStackScanPosition();
            System.out.println(String.format("stack up on stack %d -> %s", scanPosition, element));
        }

        System.out.println("----------------- STACK 3 --------------");
        Stack stackDemo3 = new Stack();
        for (int y = 0; y < 5; y++) {
            stackDemo3.add(String.format("[%d] item", y + 1));
        }
        i = 0;
        for (String element: stackDemo3.getStack()) {
            System.out.printf("- [%d] - %s\n", i, element);
            i ++;
        }

        System.out.println("----------------- Stack up! --------------");
        for (int y = 0; y < 10; y++ ){
            String element = stackDemo3.stackUp();
            int scanPosition = stackDemo3.getStackScanPosition();
            System.out.println(String.format("stack up on stack %d -> %s", scanPosition, element));
        }

        System.out.println(String.format("Current Stack element %d -> %s", stackDemo3.getStackScanPosition(), stackDemo3.currentStackElement()));
        System.out.println(String.format("Top: %s | Stack: %s | Result:\nIndex -> %d, current Stack position -> %d is stack position index? %s", 
            stackDemo3.top(), stackDemo3.currentStackElement(), stackDemo3.getIndex(), stackDemo3.getStackScanPosition(), stackDemo3.isCurrentStackPositionTop()));
    }

    

    
}

// TODO: Check if Stack is thread save (may need to add syncrhonized or volatile here and there), to some testings!

/**
 *
 * Minimalistic Stack implementation
 * It uses an index as 'cursor' to identify the current latest element added in the stack (therefore being at the top of the stack)
 * <p></p>
 * We can go through the stack via <strong><code>stackDown</code></strong> method which automatically wrap back up to the top element,
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

        size = maxSize;
        stack = new String[size];
    }

    public synchronized void add(String element) {
        indexWrap();
        stackPut(index, element);
        stackScanPosition = index; // when adding a new element, the stackScanPosition reset. This can be changed depending on use case
        index ++;
    }

    public String top() {
        return stackGet(getIndex());
    }

    public String bottom() {
        String element = stackGet(index);
        if (element == null)
            element = stackGet(0);
        return element;
    }

    public String currentStackElement() {
        return stackGet(getStackScanPosition());
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
    public synchronized String stackDown() {
        String element = stackGet(stackScanPosition);
        if (element == null) {
            stackScanPosition = getIndex();
            element = stackGet(stackScanPosition);
        }

        stackScanPosition --;
        stackScanPositionWrapDown(); 
        return element;
    }

    /**
     * Same as stackDown but goes on opposite direction
     * @return String 
     */
    public synchronized String stackUp() {
        String element = stackGet(stackScanPosition);
        if (element == null) {
            stackScanPosition = 0;
            element = stackGet(stackScanPosition);
        }

        stackScanPosition ++;
        stackScanPositionWrapUp(); 
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

    public boolean isCurrentStackPositionTop() {
        return getStackScanPosition() == getIndex();
    }

    private synchronized void indexWrap() {
        if (index + 1 > size)
            index = 0;
    }

    private synchronized void stackScanPositionWrapDown() {
        if (stackScanPosition < 0) {
            stackScanPosition = size - 1;
        }
    }

    private synchronized void stackScanPositionWrapUp() {
        if (stackScanPosition + 1 > size) {
            stackScanPosition = 0;
        }
    }

    private synchronized void stackPut(int index, String element) {
        stack[index] = element;
    }

    private String stackGet(int position) {
        try {
            return stack[position];
        } catch (ArrayIndexOutOfBoundsException ignored) {
            return null;
        }
    }
        
}