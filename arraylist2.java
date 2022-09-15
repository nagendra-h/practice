package practice;
import java.util.*;
public class arraylist2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s=new Scanner(System.in);
		int[][] x= {{1,2,3},{4,5,6}};
		int[][] b= {{{1,2,4,6},{7,8,4,1}},{6,7,9}};
		System.out.println(x[0][2]);
		int a[] = new int[9];
		int y=0;
		for (int i=0;i<8;i++) {
			System.out.println("number ");
			a[i]=s.nextInt();
			y++;
		}
		System.out.println(y);
		int m=0;
		int k=a[0];
		for(int i=1;i<y;i++) {
			if(k<a[i]) {
				k=a[i];
			}}
		m=a[0];
			for(int j=1;j<y;j++) {
				if(a[j]!=k && a[j]>m) {
					m=a[j];
				}
			}
			
		
		System.out.println(m);

	}

}
