
public class Ex5 {

	public static void main(String[] args) {
		boolean bool = true;
		System.out.println(bool);
		bool = false;
		System.out.println(bool);
		
		
	//정수 : byte, short, int, long
	//실수 : float, double
	//문자 : char
	//문자열 :String
	//논리값 : boolean
		
		//기본 데이터 타입과 사용자 정으 ㅣ데이터 타입
		//기본 테이터타입 - 자바 개발자가 만들어준 데이터의 형테
		//사용자 정의 데이터타입- 우리같은 개발자가 필요에 의해서 만든 데이터 타입
		//위 데이터 타입중 String을 제외한 8개가 자바에서의 기본 데이터 타입임
		//String은 사용자 정의 데이터타입임
		
		//기본 데이터 타입은 대입 연산자만을 사용해서 데이터를 저장할 수 있다.
		//사용자 정의 데이터타입은 대입 연산자와 new연산자 두가지를 사용해야 데이터를 저장할 수 있다.
		//사용자 정의 데이터타입은 직접적으로 데이터를 가지고 있는게 아니라 간접적으로 데이터를 가지고 있다,
		/**
		 * 변수 -형변환
		 * 데이터 타입을 바꾸는 방법
		 * 정수 ->정수
		 * 실수 ->실수
		 * 정수 ->실수
		 * 정수 ->문자
		 * 실수 ->문자
		 * 가 있는데 값의 연산에서 매우 유용하게 사용
		 * 형변환 타입 변수B = 변수A
		 * 를보면 B라는변수에 A라는변수에 저장을하는데 이때 형변환을 하면
		 * B라는 변수에 A라는변수가 B라는 변수의 형태에 맞게 저장을 해라라는 뜻
		 * 원래의 데이터에서 다른형태의 데이터로 잠시 바꿀때 형변환을 쓴다
		 * 
		 * */
		
		int num1 = 20;
		double num2= 17.3149;
		
		System.out.println((double) num1);
		System.out.println((int)num2);
		
		double num3 = (double) num1;
		int num4 = (int) num2;
		System.out.println(num3);
		System.out.println(num4);
				
		
		
		
		
		
	}

}
