import java.io.IOException;

public class ExecPy {
    public static void main(String[] args){
        Process proc;
        String compiler = "E:\\python3.8\\python.exe";
        String rootPath = "D:\\study\\DataScienceFoundation\\spider_note\\分词\\auto_note\\noteCode\\";
        String program = "main.py";
        try{
            String command = compiler + " " + rootPath + program;
            proc = Runtime.getRuntime().exec(command);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
