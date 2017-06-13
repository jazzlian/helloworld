import java.lang.String;
import java.lang.System;
import java.lang.Exception;

public final class  helloworld
{
    private final static String msg = new String("HelloWorld");

	public static void main(String[] args) throws Exception {
		
	    helloworld sample = new helloworld();
        sample.printHello();

	}

    public void printHello() {
        System.out.println(msg);
    }
}
