
package aplicacion_2;


public class Aplicacion_2 {

    public static void main(String[] args) {
        String v1, v2;
        int i =-3;
        byte b=5;
        float f= 1e-10f;
        double d=3.14;
        boolean b1 = i>b;
        boolean b2 = i<b;
        boolean b3 = b<=f;
        boolean b4 = f>=d;
        boolean b5 = d!=0;
        boolean b6 = 1==f;
        System.out.println("b1;"+i+">"+i+"="+b1);
        System.out.println("b2;"+i+"<"+b+"="+b2);
        System.out.println("b3;"+b+"<="+f+"="+b3);
        System.out.println("b4;"+f+">="+d+"="+b4);
        System.out.println("b5;"+d+"!="+0+"="+b5);
        System.out.println("b6;"+1+"=="+f+"="+b6);
        
        v1 = "a";
        v2 = "b";
        
        boolean v3 = v1!=v2;
        System.out.println("v1 es mayor v2: " +v3);
    }
    
}
