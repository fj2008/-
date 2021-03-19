
public class ex9 {

	public static void main(String[] args) {
		
		/*데이터의 크기는
		 * 실수 >정수 >문자 이런식임
		 * 업캐스팅 : 값이 작은 범위에서 큰 범위로의 형 변환(형 변환 타입 생략가능함)
		 * 다운캐스팅 : 값이 큰 범위에서 작은 범위로의 형 변환 (형 변환 타입 생략 불가능)*/
//		
//		
//		char monja = 'a';
//		int num = 20;
//		//문자를 정수로 변환 (업캐스팅)
//		int num2 = monja;
//		//정수를 실수로 변환 (업캐스팅)
//		float fNum2 = num;
//		
//		
//		//다운 캐스팅은 작은곳에서 큰곳으로 이동하기 때문에 타입을 넣어줘야함
//		char var = (char)num;
		double a = 1.1414;
		int b =(int) a;
		//정수에서 실수로 형변환
		//업캐스팅
		//없음
		int c =1;
		double d =  c;
		
		//문자에서 정수로 형변환
		//업캐스팅
		//값의 변경 없음
		char e = 'a';
		int f =  e;
		
		//정수에서 문자로 형변환
		//다운캐스팅
		//변경있음
		int g = 100;
		char h = (char)g;
		
		
		
	}

}
