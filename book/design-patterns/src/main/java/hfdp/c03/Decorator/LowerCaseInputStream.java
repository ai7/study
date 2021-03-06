/**
 * 
 */
package hfdp.c03.Decorator;

import java.io.FilterInputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 * Another Exercise in decorator to convert all chars to lower case in
 * the input stream.
 */
public class LowerCaseInputStream extends FilterInputStream {

    /**
     * @param arg0
     */
    public LowerCaseInputStream(InputStream arg0) {
	super(arg0);
	// TODO Auto-generated constructor stub
    }
    
    @Override
    public int read() throws IOException {
	int c = super.read();
	return (c == -1? c : Character.toLowerCase((char) c));
    }
    
    @Override
    public int read(byte []b, int offset, int len) throws IOException {
	int result = super.read(b,  offset,  len);
	for (int i = offset; i < offset+result; i++) {
	    b[i] = (byte) Character.toLowerCase((char) b[i]);
	}
	return result;
    }
}
