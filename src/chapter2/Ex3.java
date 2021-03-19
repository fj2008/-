package chapter2;

import java.util.Arrays;

public class Ex3 {

	public static void main(String[] args) {
		//배열의 선언과 저장
		// 데이터타입 []변수명 = new 데이터타입[]{요소1,요소2,요소3,,,,}
//		int [] korArr = new int[] {94,92,95,94};
//		double[] avgArr = {29,59.5,34,50};
//		char [] gradeArr = {'b','b','d','s'};
//		System.out.println(Arrays.toString(korArr));
//		System.out.println(Arrays.toString(avgArr));
//		System.out.println(Arrays.toString(gradeArr));
		//Arrays.toString는 배열에 관련된 기능꾸러미 사용하면 Scanner처럼 기능을 추가해서 사용할 수있다 
		
		
		//가계부 작성 프로그램을 개발 하려고 한다.
		String [] date = new String[] {"3월2일","3월3일","3월4일","3월5일","3월6일"};
		int [] don = new int [] {32159,25157,87982,40839,15908};
		char[] a = new char [] {'B','A','D','B','A'};
		System.out.println(date[0]+ date[1]+ date[2]+date[3]+date[4]);
		System.out.println(don);
		System.out.println(a);
		
		
		
		
		
		
	}

}
