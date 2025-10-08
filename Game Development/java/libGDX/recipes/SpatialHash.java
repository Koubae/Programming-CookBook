public class SpatialHash {
    private final int cellSize; // world units per cell
    private final ObjectIntMap<Long> head = new ObjectIntMap<>(); // cellKey -> index of first
    private final IntArray next = new IntArray(false, 1024);      // linked list
    private final LongArray keys = new LongArray(false, 1024);    // cellKey per entity index

    public SpatialHash(int cellSize) { this.cellSize = cellSize; }

    public void begin(int count) {
        head.clear();
        next.clear();   next.ensureCapacity(count);   next.size = count;
        keys.clear();   keys.ensureCapacity(count);   keys.size = count;
        for (int i = 0; i < count; i++) next.set(i, -1);
    }

    public void insert(int idx, float x, float y) {
        long key = keyOf(x, y);
        int oldHead = head.get(key, -1);
        next.set(idx, oldHead);
        head.put(key, idx);
        keys.set(idx, key);
    }

    public interface Visitor { void visitCell(int firstIndex); }

    public void forEachNeighbors(float x, float y, Visitor consumer) {
        int cx = (int)Math.floor(x / cellSize);
        int cy = (int)Math.floor(y / cellSize);
        for (int oy = -1; oy <= 1; oy++) {
            for (int ox = -1; ox <= 1; ox++) {
                long key = pack(cx + ox, cy + oy);
                int headIdx = head.get(key, -1);
                if (headIdx != -1) consumer.visitCell(headIdx);
            }
        }
    }

    public int nextOf(int idx) { return next.get(idx); }

    private long keyOf(float x, float y) {
        int cx = (int)Math.floor(x / cellSize);
        int cy = (int)Math.floor(y / cellSize);
        return pack(cx, cy);
    }
    private static long pack(int x, int y) { return (((long)x) << 32) ^ (y & 0xffffffffL); }
}
