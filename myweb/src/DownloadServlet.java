import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 *  文件下载
 *  1.需要通过response.setContentType方法设置Content-type头字段的值，
 *  为浏览器无法使用某种方式或激活某个程序来处理的MIME类型。application/octet-stream或者application/x-msdownload
 *  2.通过response.setHeader方法设置Content-Disposition头的值为"attachment;filename=文件名"
 *  3.读取下载文件。调用response.getOutputStream方法向客户端写入附件内容。
 */
@WebServlet("/downloadServlet")
public class DownloadServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("文件下载。。。");

        //设置请求编码格式
        response.setContentType("text/html;charset=UTF-8");
        request.setCharacterEncoding("UTF-8");
        //获取参数（得到要下载的文件名）
        String fileName = request.getParameter("fileName");
        //参数非空判断
        if (fileName == null || "".equals(fileName.trim())){
            response.getWriter().write("请输入要下载的文件名!");
            response.getWriter().close();
            return;
        }
        //得到图片存放的路径
        String path = request.getServletContext().getRealPath("/download/");

        // 通过路径得到file对象
        File file = new File(path+fileName);

        //判断文件对象是否存在并且是一个标准文件
        if (file.exists() && file.isFile()){
            //设置响应类型 （浏览器无法激活的响应类型）
            response.setContentType("application/x-msdownload");
            //设置响应头信息
            response.setHeader("Content-Disposition","attachment;filename="+fileName);
            //得到file文件输入流
            InputStream in = new FileInputStream(file);
            //得到字节输出流
            ServletOutputStream out = response.getOutputStream();
            //定义byte数组
            byte[] bytes = new byte[1024];
            int len = 0;
            //循环输出
            while ((len = in.read(bytes))!= -1){
                //输出
                out.write(bytes,0,len);
            }
            //关闭资源
            out.close();
            in.close();
        }
        else {
            response.getWriter().write("文件不存在，请重试！");
            response.getWriter().close();
        }
    }
}
