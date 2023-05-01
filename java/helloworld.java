import java.lang.String;
import java.lang.System;

public final class  helloworld
{
    private final static String msg = "HelloWorld";

	public static void main(String[] args) {
		
	    helloworld sample = new helloworld();
        sample.printHello();

	}

    public void printHello() {
        System.out.println(msg);
    }
}
