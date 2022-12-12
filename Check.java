package sample;
import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.*;

import org.junit.jupiter.api.Test;


public class Check {
	@Test
	public void fact(int n) {
		int s=0;
		int f=1;
		for(int i=1;i<=n;i++) {
			f=f*i;
		}
		s=s+f;
		System.out.println(s);
	}
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String s9="hello hey";
		Check c1=new Check();
		c1.fact(3);
		System.out.println("----------------");
		String[] s8=s9.split(" ");
		System.out.println(" heyyyy" +s8[0]);

		System.out.println("enter the string");
		String s1=s.next();
		char s2;
	    char[] s4=new char[100];
		s2=s1.charAt(0);
		int i=s1.length();
		char s3=s1.charAt(i-1);
		System.out.println(s3);
		int j=1;
		System.out.println(s1.charAt(0));
		for(int i1=i-2;i1>=1;i1--) {
			s4[j]=s1.charAt(i1);
			j =j+1;
		}
		s4[0]=s2;
		s4[j]=s3;
		System.out.println(s4);
		
	}

}
