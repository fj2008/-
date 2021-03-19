package chapter2;

import java.util.Scanner;

public class Ex2 {

	public static void main(String[] args) {
		//배열에 저장할 데이터의 갯수는 전통적으로 상수만 가능한데
		//자바는 특별히 변수도 넣을 수 있음
		//컴파일 타임에 배열의 크기를 결정한다.
		char [] arr1 = new char[2];
		//위와같은 경우는 상수를 쓰기때문에 고정적임
		
		System.out.println("배열의 갯수 : ");
		Scanner scanf = new Scanner(System.in);
		
		int length = scanf . nextInt();
		char[] arr1_1 = new char [length];
		//위와같은 경우는 런타임에 입력하는 수에 때라서 배열의 크기가 달라짐.
		// 동정 배열 생성 이라고도 한다
		
	}

}
