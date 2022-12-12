package sample;
class exten extends Lab1{
	exten(){
		System.out.println();
	}
	public exten(exten e2) {
		System.out.println("          ++++++++++++++" + e2.sno+e2.m1);
		e2.dis(121,"ram",44,55);
	}
}
public class Lab1 {
	protected int m1,m2,m3,m4;
	static String sname,course;
	public int sno;
	public Lab1() {
		sno=100009999;
		m1=60;
		m2=70;
		course="MCA";
	}
	public Lab1(String s,int m3,int m4) {
		sname=s;
		this.m3=m3;
		this.m4=m4;
	}
	protected void dis(int sno,String s,int m1,int m2) {
		System.out.println("sno,name,mark1,mark2"+sno+s+m1+m2);
	}
	public void dis(String c,int m3,int m4) {
		System.out.println("course,mark3,mark4"+"    "+c+m3+m4);
	}
	public static void main(String[] args) {
		Lab1 l1=new Lab1();
		Lab1 l2=new Lab1("ram",60,70);
		exten e1 = new exten();
		exten e2=new exten(e1);
		System.out.println("sjdhfsjd"+e1.sno);
				
		l1.dis(l1.sno,Lab1.sname,l1.m1,l1.m2);
		l2.dis(Lab1.course,l2.m3,l2.m4);
		
		

	}

}
