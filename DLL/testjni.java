public class testjni2
{
  static
  {
    System.loadLibrary("native"); //loading sharing libraary   //loading native automatic dll includede
    
  }
  public static void main(String[] args) {
    System.out.println("Addition is "+new tstjni2().add(20,40));
  }
  private native int add(int n1,int n2);


}