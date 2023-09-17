// Copyright 2015 Christian d'Heureuse, Inventec Informatik AG, Zurich, Switzerland
// www.source-code.biz, www.inventec.ch/chdh
//
// This module is multi-licensed and may be used under the terms of any of the following licenses:
//
//  LGPL, GNU Lesser General Public License, V2.1 or later, http://www.gnu.org/licenses/lgpl.html
//  EPL, Eclipse Public License, V1.0 or later, http://www.eclipse.org/legal
//
// Please contact the author if you need another license.
// This module is provided "as is", without warranties of any kind.
//
// Home page: http://www.source-code.biz/snippets/java/RawConsoleInput

package biz.source_code.utils;

import java.io.InputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.nio.charset.CodingErrorAction;
import java.util.Arrays;
import java.util.List;
import com.sun.jna.LastErrorException;
import com.sun.jna.Library;
import com.sun.jna.Native;
import com.sun.jna.Structure;
import com.sun.jna.Pointer;
import com.sun.jna.ptr.IntByReference;

/**
 * A JNA based driver for reading single characters from the console.
 *
 * <p>This class is used for console mode programs.
 * It supports non-blocking reads of single key strokes without echo.
 */
public class RawConsoleInput {

    private static final boolean           isWindows     = System.getProperty("os.name").startsWith("Windows");
    private static final int               invalidKey    = 0xFFFE;
    private static final String            invalidKeyStr = String.valueOf((char)invalidKey);

    private static boolean                 initDone;
    private static boolean                 stdinIsConsole;
    private static boolean                 consoleModeAltered;

    /**
     * Reads a character from the console without echo.
     *
     * @param wait
     *   <code>true</code> to wait until an input character is available,
     *   <code>false</code> to return immediately if no character is available.
     * @return
     *   -2 if <code>wait</code> is <code>false</code> and no character is available.
     *   -1 on EOF.
     *   Otherwise an Unicode character code within the range 0 to 0xFFFF.
     */
    public static int read (boolean wait) throws IOException {
        if (isWindows) {
            return readWindows(wait); }
        else {
            return readUnix(wait); }}

    /**
     * Resets console mode to normal line mode with echo.
     *
     * <p>On Windows this method re-enables Ctrl-C processing.
     *
     * <p>On Unix this method switches the console back to echo mode.
     * read() leaves the console in non-echo mode.
     */
    public static void resetConsoleMode() throws IOException {
        if (isWindows) {
            resetConsoleModeWindows(); }
        else {
            resetConsoleModeUnix(); }}

    private static void registerShutdownHook() {
        Runtime.getRuntime().addShutdownHook( new Thread() {
            public void run() {
                shutdownHook(); }}); }

    private static void shutdownHook() {
        try {
            resetConsoleMode(); }
        catch (Exception e) {}}

//--- Windows ------------------------------------------------------------------

// The Windows version uses _kbhit() and _getwch() from msvcrt.dll.

    private static Msvcrt        msvcrt;
    private static Kernel32      kernel32;
    private static Pointer       consoleHandle;
    private static int           originalConsoleMode;

    private static int readWindows (boolean wait) throws IOException {
        initWindows();
        if (!stdinIsConsole) {
            int c = msvcrt.getwchar();
            if (c == 0xFFFF) {
                c = -1; }
            return c; }
        consoleModeAltered = true;
        setConsoleMode(consoleHandle, originalConsoleMode & ~Kernel32Defs.ENABLE_PROCESSED_INPUT);
        // ENABLE_PROCESSED_INPUT must remain off to prevent Ctrl-C from beeing processed by the system
        // while the program is not within getwch().
        if (!wait && msvcrt._kbhit() == 0) {
            return -2; }                                         // no key available
        return getwch(); }

    private static int getwch() {
        int c = msvcrt._getwch();
        if (c == 0 || c == 0xE0) {                              // Function key or arrow key
            c = msvcrt._getwch();
            if (c >= 0 && c <= 0x18FF) {
                return 0xE000 + c; }                              // construct key code in private Unicode range
            return invalidKey; }
        if (c < 0 || c > 0xFFFF) {
            return invalidKey; }
        return c; }                                             // normal key

    private static synchronized void initWindows() throws IOException {
        if (initDone) {
            return; }
        msvcrt = Native.load("msvcrt", Msvcrt.class);
        kernel32 = Native.load("kernel32", Kernel32.class);
        try {
            consoleHandle = getStdInputHandle();
            originalConsoleMode = getConsoleMode(consoleHandle);
            stdinIsConsole = true; }
        catch (IOException e) {
            stdinIsConsole = false; }
        if (stdinIsConsole) {
            registerShutdownHook(); }
        initDone = true; }

    private static Pointer getStdInputHandle() throws IOException {
        Pointer handle = kernel32.GetStdHandle(Kernel32Defs.STD_INPUT_HANDLE);
        if (Pointer.nativeValue(handle) == 0 || Pointer.nativeValue(handle) == Kernel32Defs.INVALID_HANDLE_VALUE) {
            throw new IOException("GetStdHandle(STD_INPUT_HANDLE) failed."); }
        return handle; }

    private static int getConsoleMode (Pointer handle) throws IOException {
        IntByReference mode = new IntByReference();
        int rc = kernel32.GetConsoleMode(handle, mode);
        if (rc == 0) {
            throw new IOException("GetConsoleMode() failed."); }
        return mode.getValue(); }

    private static void setConsoleMode (Pointer handle, int mode) throws IOException {
        int rc = kernel32.SetConsoleMode(handle, mode);
        if (rc == 0) {
            throw new IOException("SetConsoleMode() failed."); }}

    private static void resetConsoleModeWindows() throws IOException {
        if (!initDone || !stdinIsConsole || !consoleModeAltered) {
            return; }
        setConsoleMode(consoleHandle, originalConsoleMode);
        consoleModeAltered = false; }

    private static interface Msvcrt extends Library {
        int _kbhit();
        int _getwch();
        int getwchar(); }

    private static class Kernel32Defs {
        static final int  STD_INPUT_HANDLE       = -10;
        static final long INVALID_HANDLE_VALUE   = (Native.POINTER_SIZE == 8) ? -1 : 0xFFFFFFFFL;
        static final int  ENABLE_PROCESSED_INPUT = 0x0001;
        static final int  ENABLE_LINE_INPUT      = 0x0002;
        static final int  ENABLE_ECHO_INPUT      = 0x0004;
        static final int  ENABLE_WINDOW_INPUT    = 0x0008; }

    private static interface Kernel32 extends Library {
        int GetConsoleMode (Pointer hConsoleHandle, IntByReference lpMode);
        int SetConsoleMode (Pointer hConsoleHandle, int dwMode);
        Pointer GetStdHandle (int nStdHandle); }

//--- Unix ---------------------------------------------------------------------

// The Unix version uses tcsetattr() to switch the console to non-canonical mode,
// System.in.available() to check whether data is available and System.in.read()
// to read bytes from the console.
// A CharsetDecoder is used to convert bytes to characters.

    private static final int               stdinFd = 0;
    private static Libc                    libc;
    private static CharsetDecoder          charsetDecoder;
    private static Termios                 originalTermios;
    private static Termios                 rawTermios;
    private static Termios                 intermediateTermios;

    private static int readUnix (boolean wait) throws IOException {
        initUnix();
        if (!stdinIsConsole) {                                  // STDIN is not a console
            return readSingleCharFromByteStream(System.in); }
        consoleModeAltered = true;
        setTerminalAttrs(stdinFd, rawTermios);                  // switch off canonical mode, echo and signals
        try {
            if (!wait && System.in.available() == 0) {
                return -2; }                                      // no input available
            return readSingleCharFromByteStream(System.in); }
        finally {
            setTerminalAttrs(stdinFd, intermediateTermios); }}   // reset some console attributes

    private static Termios getTerminalAttrs (int fd) throws IOException {
        Termios termios = new Termios();
        try {
            int rc = libc.tcgetattr(fd, termios);
            if (rc != 0) {
                throw new RuntimeException("tcgetattr() failed."); }}
        catch (LastErrorException e) {
            throw new IOException("tcgetattr() failed.", e); }
        return termios; }

    private static void setTerminalAttrs (int fd, Termios termios) throws IOException {
        try {
            int rc = libc.tcsetattr(fd, LibcDefs.TCSANOW, termios);
            if (rc != 0) {
                throw new RuntimeException("tcsetattr() failed."); }}
        catch (LastErrorException e) {
            throw new IOException("tcsetattr() failed.", e); }}

    private static int readSingleCharFromByteStream (InputStream inputStream) throws IOException {
        byte[] inBuf = new byte[4];
        int    inLen = 0;
        while (true) {
            if (inLen >= inBuf.length) {                         // input buffer overflow
                return invalidKey; }
            int b = inputStream.read();                          // read next byte
            if (b == -1) {                                       // EOF
                return -1; }
            inBuf[inLen++] = (byte)b;
            int c = decodeCharFromBytes(inBuf, inLen);
            if (c != -1) {
                return c; }}}

    // (This method is synchronized because the charsetDecoder must only be used by a single thread at once.)
    private static synchronized int decodeCharFromBytes (byte[] inBytes, int inLen) {
        charsetDecoder.reset();
        charsetDecoder.onMalformedInput(CodingErrorAction.REPLACE);
        charsetDecoder.replaceWith(invalidKeyStr);
        ByteBuffer in = ByteBuffer.wrap(inBytes, 0, inLen);
        CharBuffer out = CharBuffer.allocate(1);
        charsetDecoder.decode(in, out, false);
        if (out.position() == 0) {
            return -1; }
        return out.get(0); }

    private static synchronized void initUnix() throws IOException {
        if (initDone) {
            return; }
        libc = Native.load("c", Libc.class);
        stdinIsConsole = libc.isatty(stdinFd) == 1;
        charsetDecoder = Charset.defaultCharset().newDecoder();
        if (stdinIsConsole) {
            originalTermios = getTerminalAttrs(stdinFd);
            rawTermios = new Termios(originalTermios);
            rawTermios.c_lflag &= ~(LibcDefs.ICANON | LibcDefs.ECHO | LibcDefs.ECHONL | LibcDefs.ISIG);
            intermediateTermios = new Termios(rawTermios);
            intermediateTermios.c_lflag |= LibcDefs.ICANON;
            // Canonical mode can be switched off between the read() calls, but echo must remain disabled.
            registerShutdownHook(); }
        initDone = true; }

    private static void resetConsoleModeUnix() throws IOException {
        if (!initDone || !stdinIsConsole || !consoleModeAltered) {
            return; }
        setTerminalAttrs(stdinFd, originalTermios);
        consoleModeAltered = false; }

    protected static class Termios extends Structure {         // termios.h
        public int      c_iflag;
        public int      c_oflag;
        public int      c_cflag;
        public int      c_lflag;
        public byte     c_line;
        public byte[]   filler = new byte[64];                  // actual length is platform dependent
        @Override protected List<String> getFieldOrder() {
            return Arrays.asList("c_iflag", "c_oflag", "c_cflag", "c_lflag", "c_line", "filler"); }
        Termios() {}
        Termios (Termios t) {
            c_iflag = t.c_iflag;
            c_oflag = t.c_oflag;
            c_cflag = t.c_cflag;
            c_lflag = t.c_lflag;
            c_line  = t.c_line;
            filler  = t.filler.clone(); }}

    private static class LibcDefs {
        // termios.h
        static final int ISIG    = 0000001;
        static final int ICANON  = 0000002;
        static final int ECHO    = 0000010;
        static final int ECHONL  = 0000100;
        static final int TCSANOW = 0; }

    private static interface Libc extends Library {
        // termios.h
        int tcgetattr (int fd, Termios termios) throws LastErrorException;
        int tcsetattr (int fd, int opt, Termios termios) throws LastErrorException;
        // unistd.h
        int isatty (int fd); }

}